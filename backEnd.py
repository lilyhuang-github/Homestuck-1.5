from flask import Flask, jsonify
from fastapi import FastAPI
from setup import character, getSimpleDialogue, loadDialogue, getAbreviation, getFullName
import json
# # d = loadDialogue(f'./ngram/TN.json')
# # print(d)
# app = Flask(__name__)
app = FastAPI()


@app.get('/api/acronym/{fn}')
def getAcronym(fn):
    return getAbreviation(fn)
@app.get('/api/fullName/{ac}')
def getFullname(ac):
    acronym = ac.strip().upper()
    return getFullName(acronym)

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
