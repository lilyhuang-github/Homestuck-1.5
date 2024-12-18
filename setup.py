import os
import json
import re
from conversions import getAbreviation, getFullName
from collections import defaultdict
import random
from odf.opendocument import load
from odf.text import P
from odf.element import Text
from typing import Self

def openODT(file):
    odt_doc = load(file)

    paragraphs = odt_doc.getElementsByType(P)
    
    text_content = []
    
    for paragraph in paragraphs:
        if paragraph.hasChildNodes():
            for child in paragraph.childNodes:
                if isinstance(child, Text) and child.data:
                    text_content.append(child.data)
    

    return "\n".join(text_content)

pattern = re.compile(r'''
    (Act\s\d+|Intermission)\s*_    
    |
    (\d+\.\s([A-Z]{2}\d+):\s=.*)   
    |
    ([^\n]+)                       
''', re.VERBOSE)


def importAbbreviations(file = "list of abbreviations.odt"):
    data = openODT(file)
    found = re.findall(r'^[A-Za-z]+[A-Za-z0-9]*\b(?=\s*=\s*)', data, re.MULTILINE )
    return found

def importFullName(file = "list of abbreviations.odt"):
    data = openODT(file)
    found = re.findall(r'(?<=\=\s)[A-Za-z0-9 ,.\'()-]+', data, re.MULTILINE )
    return found
# print(importAbbreviations())

def extractJSON(file):
    matches = openODT(file)
    # matches  = pattern.findall(openODT(file))
    abbreviations = importAbbreviations()
    #gets a list of the character's abbreviations

    # regex to find the line
    regexp = re.compile(r'\..{2,4}: =', re.IGNORECASE)
    regexp2 = re.compile("[A-Z]{2,4}", re.IGNORECASE)    
    dict = defaultdict(list)

    currentChar = ""
    for x in matches.splitlines():
    #adds the line to the dict
        if not currentChar == "" and not x == "_":
            dict[currentChar].append("<s> " + x + " </s>")
        if regexp.search(x):
            # print(x)
            #changes who the dictionary points at
            match = (re.search(regexp2, x))
            if match:
                currentChar = match.group()
                # print(currentChar)
        if x == "_":
            currentChar = ""
        

        
        # print(x)
    # print(dict)
    return dict

def tokenizeAll(dictionary):
    # dict = defaultdict(list)
    dict = {}
    for x in dictionary:
        # print(x)
        dict[x] = []
        for y in dictionary[x]:
            for z in (tokenize(y)):
                dict[x].append(z)
    return dict
def tokenize(text):
    tokens = text.split()
    # tokens = re.findall(r'\s*', text)
    return tokens
def generateNgram(tokens) ->json:
    # ngram_model = defaultdict(list)
    ngram_model = defaultdict(lambda: defaultdict(lambda:defaultdict(int)))
    # ngram_model = defaultdict(lambda: defaultdict(int))
    # print(ngram_model)

    #creates a nested dictionary for each word and pair
    #so it'd be like A: {B: 1}
    # B: {C: 1}
    for keys in tokens:
        for value in range(len(tokens[keys]) - 1):
            context = tokens[keys][value]
            next_word = tokens[keys][value + 1]
            # print(context, next_word)
            ngram_model[keys][context][next_word] += 1
        # pass
        # print(keys)
        # print(tokens[keys][0])
        # for values in tokens[keys]:
            
    # for i in range(len(tokens) - 1):
        

    #     context = tokens[i]
    #     next_word = tokens[i + 1]
    #     ngram_model[context][next_word] += 1
    # print(ngram_model)
    return ngram_model
# def genAllNGrams(tokens):
#     ngram = defaultdict(list)
#     for x in tokens:
#         ngram[x].append(generateNgram(tokens[x]))
#     return ngram

def saveDialogue(chats, file):
    with open(file, 'w', encoding='utf-8') as file:
        json.dump(chats, file)
def loadDialogue(file):
    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def predict_next_word(speaker:json, listener:str, previous_word:str) ->str:
    #access the dictionaries key value pair
    next_word_frequencies = speaker[listener].get(previous_word, {})
    # print(next_word_frequencies)
    if not next_word_frequencies:
        return None  # No valid next word for this context


    #every possible option based on previous word 
    words = list(next_word_frequencies.keys())

    #gets the value/weighting off it all
    weights = list(next_word_frequencies.values())
    

    #makes a choice randomly
    next_word = random.choices(words, weights=weights, k=1)[0]
    return next_word

def predictSentence(speakerNgram:json, listenerAbv:str) -> str:
    # ngram_model = loadNgram("nGram.json")
    # Example: predict the next word after "<s>"
    nextWord = "<s>"
    sentence = ""
    while not nextWord == "</s>":
        sentence += " " + nextWord
        nextWord = predict_next_word(speakerNgram, listenerAbv, nextWord)
        # print(nextWord)
    sentence = sentence[5:]
    return sentence
def firstTimeSetup(): #sets up all the characters that are in the ODT directory
    for file in os.listdir("charactersODT"):
        name = file.split(".")[0]
        ngram = singleSetup("./charactersODT/" + file)
        saveDialogue(ngram, os.path.join("./ngram/", getAbreviation(name)+ ".json"))


def singleSetup(file:str) ->json: #sets up a single character based on an odt file 
    text = extractJSON(file)
    token = tokenizeAll(text)
    ngram = generateNgram(token)
    return ngram

def getDialogue(speakerNgram:json, speakerAbv:str, listenerAbv:str) -> str:
    return getFullName(speakerAbv) + ": " + predictSentence(speakerNgram, listenerAbv)

def dialogueOnce(speakerNgram:json, listenerNgram:json, speakerAbv:str, listenerAbv:str):
    r = random.randint(1,2)
    speakerConv = getAbreviation(speakerAbv) 
    match r:
        case 1:
            return getDialogue(speakerNgram, speakerAbv, listenerAbv)
        case 2:
            return getDialogue(listenerNgram, listenerAbv, speakerAbv)
        case _:
            return None
# def getSimpleDialogue2(*character, iter = None):

def getSimpleDialogue(*character, iter = None) ->None:
    for x in range(0,len(character)-1):
        for y in range(x+1, len(character)):
            if character[y].abrev in character[x].ngram:
                pass
                #passes test i.e the character has dialogue with the other character
            else:
                raise Exception("Character doesn't have valid dialogue with each other " +  character[y].fullName + "and " + character[x].fullName)
    if iter == None:
        iter = len(character)
    for x in range(iter):
        r = random.randint(0, len(character)-1) # get talking character
        l = random.choice([x for x in range(0, len(character)-1) if x != r]) # get listener character
        print(getDialogue(character[r].ngram, character[r].abrev, character[l].abrev))


def getSoloDialogue(speakerNgram:json, speakerAbv:str) ->str:
    x = random.choice([x for x in speakerNgram])
    
    return getDialogue(speakerNgram, speakerAbv, x)
class character:
    def __init__(self, ngram:json, abrev:str):
        self.ngram = ngram
        self.abrev = abrev
        self.fullName = getFullName(abrev)
        
    @classmethod
    def fromFile(self, file:str, abrev:str):
        # print(file)
        f = loadDialogue(file)
        return character(f, abrev)

        #character if they talked to themselves
    def getRandomDialogue(self)->str:
        return getSoloDialogue(self.ngram, self.abrev)
    
    #character talking to another character
    def talkToCharacter(self, character:Self) ->str:
        return getDialogue(self.ngram, self.abrev, character.abrev)
    
    #character talking back and forth with another character
    def talkToCharacterBackForth(self, character, iter=5):
        dialogue = ""
        for x in range(iter):
            r = random.randint(0,1)
            if r == 1:
                dialogue += f'{character.talkToCharacter(self)}\n'
            else:
                dialogue += f'{self.talkToCharacter(character)}\n'
        return dialogue
    
    #talk to any number of characters
    def talkToAnyCharacters(self, *characters, iter=5):
        dialogue = ""
        # print(characters[0])
        for x in range(iter):
            r = random.randint(0, len(characters))
            # print(r)
            # print([x for x in range(0,len(characters)+1)])
            l = random.choice([x for x in range(0, len(characters)+1) if x != r])
            # print(f'r: {r} , l:{l}')
            if r ==0 or l ==0:
                if r ==0:
                    dialogue += f'{self.talkToCharacter(characters[l-1])}\n'
                if l ==0:
                    dialogue += f'{characters[r-1].talkToCharacter(self)}\n'
            else:
                dialogue += f'{characters[r-1].talkToCharacter(characters[l-1])}\n'
        return dialogue
    

firstTimeSetup()
# def 
# firstTimeSetup()
# t = loadDialogue("./ngram/TP.json")
# c4 = character(t, "TP")
# print(c4.getRandomDialogue())
# d = loadDialogue("./ngram/VS.json")
# getSimpleDialogue(d)
# d.getRandomDialogue()
# s = loadDialogue("./ngram/TN.json")
# a = loadDialogue("./ngram/AM.json")
# c = character(s, "TN")
# c = character.fromFile("./ngram/TN.json", "TN")
# print(c.ngram)
# print(c.abrev)
# c2 = character(d, "VS")
# print(c2.getRandomDialogue())
# c1 = character(a, "AM")
# c3 = character(s, "TN")
# print(c2.talkToAnyCharacters(c3, c1, iter=10))
# print(c2.talkToCharacterBackForth(c3))
# print(c2.talkToCharacter(c3))
# print(c3.talkToCharacter(c2))
# print(c3.getRandomDialogue())
# getSimpleDialogue((c2,c3))
# print(getSoloDialogue(c.ngram, "VS"))
# getSimpleDialogue(c, c2, c3, iter=10)
# if "TN" in c2.ngram:
#     print("IT WORKS")
# for x in range(10):
#     print(dialogueOnce(d, s, "VS", "TN"))
# print(d.keys())
# v =extractJSON("vriska serket.odt")
# x = tokenizeAll(v)
# test = (loadDialogue("TEST123.json"))
# print(x)
# z = generateNgram(x)
# print(predictSentence(z, "TN"))
# saveDialogue(z, "TEST123.json")
# print(z)
# abv = importAbbreviations()
# print(abv)
# print(x)
# links = list(v.keys())
# print(links)
# saveDialogue(v, "Vriska.json")
# print(extractJSON("vriska serket.odt"))
# print(openODT("vriska serket.odt"))