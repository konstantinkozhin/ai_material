from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
from fastai.vision.all import *
from fastapi import FastAPI, UploadFile, File, Body, Depends, HTTPException, status
import shutil
import os
from fastapi.security import OAuth2PasswordBearer



app = FastAPI()

@app.post('/collection_1/material')

async def root(file: UploadFile = File(...)):
    
    with open(f'{file.filename}','wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    learn = load_learner('model2.pkl')
    result = list(learn.predict(item=file.filename))

    name_pred = str(result[1])
    name_pred = int(name_pred[name_pred.find('(')+1:name_pred.find(')')])
    perc_pred = str(result[2][name_pred])
    perc_pred = round(float(perc_pred[perc_pred.find('(')+1:perc_pred.find(')')]),2)

    os.remove(file.filename)

    if result[0] == "бронза" and perc_pred >= 0.9:
        return {"material": result[0].title()}

    elif result[0] == "глина" and perc_pred >= 0.9:
        return {"material": result[0].title()}

    elif result[0] == "железо" and perc_pred >= 0.9:
        return {"material": result[0].title()}

    elif result[0] == "камень" and perc_pred >= 0.9:
        return {"material": result[0].title()}

    elif result[0] == "керамика" and perc_pred >= 0.9:
        return {"material": result[0].title()}

    elif result[0] == "кость" and perc_pred >= 0.9:
        return {"material": result[0].title()}

    elif result[0] == "медь" and perc_pred >= 0.9:
        return {"material": result[0].title()}

    else:
        return {}


