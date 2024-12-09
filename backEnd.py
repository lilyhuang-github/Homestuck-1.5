from flask import Flask, jsonify
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
    allow_origins=origins,
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

# if __name__ == '__main__':
#     app.run()

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/api/data")
# def read_data():
#     return {"message": "Hello from Python backend!"}
