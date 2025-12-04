from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from setup import character, getSimpleDialogue, loadDialogue, getAbreviation, getFullName
from conversions import getFullName
import json
from os import listdir
# # d = loadDialogue(f'./ngram/TN.json')
# # print(d)
# app = Flask(__name__)
app = FastAPI()
origins = [
    "http://localhost:5173/",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def test():
    return {"apiEndPoint":"works"}
@app.get('/api/acronym/{fn}')
def getAcronym(fn):
    return getAbreviation(fn)
@app.get('/api/fullName/{ac}')
def getFullname(ac):
    acronym = ac.strip().upper()
    return getFullName(acronym)

@app.get('/api/available')
def getAvailableCharacters(): 
    d = listdir("ngram")
    characters = {}
    for x in d:
        abrev = x.split(".")[0]
        characters[abrev] = getFullName(abrev)
        # characters.append(x.split(".")[0])
        # characters.splitappend(x)
    return characters
   
#test 2 2 2

@app.get('/api/character/{chr}')
def get_data(chr):
    
    # print(f"wasd {c} wasd")
    d = loadDialogue(f'./ngram/{chr}.json')
    char = character(d, chr)
    # get = character.fromFile(f'./ngram/{c}.json')
    # return (char)
    # print(char)
    # return({
    #     "ngram":char.ngram,
    #     "abrev":char.abrev,
    #     "fullName":char.fullName
    # })
    return(char)
#gets 1 instance of dialogue from the character
@app.get('/api/get1dialogue/{chrs}')
def getdialogues(chrs):
    d = loadDialogue(f'./ngram/{chrs}.json')
    c2 = character(d, f'{chrs}')
    # print(c2.getRandomDialogue())
    return c2.getRandomDialogue()
    # return d

#gets 2 characters with their dialogue in format of :character,character
@app.get('/api/get2dialogue/{chrs}')
def get2dialogues(chrs):
    x = chrs.split(',')
    d = loadDialogue(f'./ngram/{x[0]}.json')
    d2 = loadDialogue(f'./ngram/{x[1]}.json')
    c = character(d, f'{x[0]}')
    c2 = character(d2, f'{x[1]}')
    return c.talkToCharacterBackForth(c2)

#gets any amount of characters with their dialogue in format of :character,character,....,number
#number representating how many iterations there should be
@app.get('/api/getxdialogue/{chrs}')
def getxdialogues(chrs):
    x = chrs.split(',')
    iterations = x[-1]
    x = x[:-1]
    characters = []
    #loops through and packs the characters into the array
    for z in range(len(x)):
        d = loadDialogue(f'./ngram/{x[z]}.json')
        characters.append(character(d, f'{x[z]}'))
    
    #gets dialogue by unpacking the array
    dialogue = characters[0].talkToAnyCharacters(*characters[1:], iter=int(iterations))
    return dialogue


# if __name__ == '__main__':
#     app.run()

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/api/data")
# def read_data():
#     return {"message": "Hello from Python backend!"}
