import os
import json
import re
from conversions import getAbreviation, getFullName
from collections import defaultdict
import random
from odf.opendocument import load
from odf.text import P
from odf.element import Text

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
    regexp = re.compile("\..{2,4}: =", re.IGNORECASE)
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
def generateNgram(tokens):
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

def predict_next_word(speaker, listener, previous_word):
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

def predictSentence(speaker, listener):
    # ngram_model = loadNgram("nGram.json")
    # Example: predict the next word after "<s>"
    nextWord = "<s>"
    sentence = ""
    while not nextWord == "</s>":
        sentence += " " + nextWord
        nextWord = predict_next_word(speaker, listener, nextWord)
        # print(nextWord)
    sentence = sentence[5:]
    return sentence
print(getAbreviation(" davest rider"))
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