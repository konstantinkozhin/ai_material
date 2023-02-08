from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
from fastai.vision.all import *
from fastapi import FastAPI, UploadFile, File, Body, Depends, HTTPException, status
import shutil
import os
from fastapi.security import OAuth2PasswordBearer
import pathlib


plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath


app = FastAPI()


@app.post('/classify')

async def root(file: bytes = File()):

    learner = load_learner("app/model.pkl")

    result = list(learner.predict(file))
    name_pred = str(result[1])
    name_pred = int(name_pred[name_pred.find('(')+1:name_pred.find(')')])
    perc_pred = str(result[2][name_pred])
    perc_pred = round(float(perc_pred[perc_pred.find('(')+1:perc_pred.find(')')]),2)

    if perc_pred >= 0.9:
        return {
            "response": 'Материал определен с высокой вероятностью',
            "result": {
                "medium": result[0].title(),
                "confidence": perc_pred
            }
        }

    # elif result[0] == "глина" and perc_pred >= 0.9:
    #     return {}

    # elif result[0] == "железо" and perc_pred >= 0.9:
    #     return {}

    # elif result[0] == "камень" and perc_pred >= 0.9:
    #     return {}

    # elif result[0] == "керамика" and perc_pred >= 0.9:
    #     return {}

    # elif result[0] == "кость" and perc_pred >= 0.9:
    #     return {}

    # elif result[0] == "медь" and perc_pred >= 0.9:
    #     return {}

    else:
        return {
            "response": 'Материал определен с низкой вероятностью',
            "result": {
                "medium": result[0].title(),
                "confidence": perc_pred
            }
        }


