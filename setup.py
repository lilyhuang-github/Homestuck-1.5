import os
import json
import re
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
    (Act\s\d+|Intermission)\s*_    # Match Acts or Intermission followed by _
    |
    (\d+\.\s([A-Z]{2}\d+):\s=.*)   # Match speaker identifier (e.g., TN1: =004022)
    |
    ([^\n]+)                       # Match the actual dialogue lines
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

    # regex to find the line
    regexp = re.compile("\..{2,4}: =", re.IGNORECASE)
    regexp2 = re.compile("[A-Z]{2,4}", re.IGNORECASE)    
    dict = defaultdict(list)

    currentChar = ""
    for x in matches.splitlines():
        if not currentChar == "" and not x == "_":
            dict[currentChar].append("<s> " + x + " </s>")
        if regexp.search(x):
            match = (re.search(regexp2, x))
            if match:
                currentChar = match.group()
        if x == "_":
            currentChar = ""
        

        
        # print(x)
    # print(dict)
    return dict

def tokenizeAll(dictionary):
    dict = defaultdict(list)
    for x in dictionary:
        for y in dictionary[x]:
            for z in (tokenize(y)):
                dict[x].append(z)
    return dict
def tokenize(text):
    tokens = text.split()
    # tokens = re.findall(r'\s*', text)
    return tokens
def generateNgram(tokens):
    ngram_model = defaultdict(lambda: defaultdict(int))
    # print(ngram_model)

    #creates a nested dictionary for each word and pair
    #so it'd be like A: {B: 1}
    # B: {C: 1}
    for i in range(len(tokens) - 1):
        context = tokens[i]
        next_word = tokens[i + 1]
        ngram_model[context][next_word] += 1
    return ngram_model
def genAllNGrams(tokens):
    ngram = defaultdict(list)
    for x in tokens:
        ngram[x].append(generateNgram(tokens[x]))
    return ngram

def saveDialogue(chats, file):
    with open(file, 'w', encoding='utf-8') as file:
        json.dump(chats, file)

v =extractJSON("vriska serket.odt")
x = tokenizeAll(v)
z = genAllNGrams(x)
print(z)
# print(x)
# links = list(v.keys())
# print(links)
# saveDialogue(v, "Vriska.json")
# print(extractJSON("vriska serket.odt"))
# print(openODT("vriska serket.odt"))