from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
from fastai.vision.all import *
             


app = FastAPI()

class ScoringItem(BaseModel):
	NameImage: str


@app.post('/')

async def scoring_endpoint(item: ScoringItem):

	df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
	namefile = df['NameImage'][0]

	learn = load_learner(r'C:\Users\IKIT-SILA\Desktop\Pr\fastml\model2.pkl')
	result = list(learn.predict(item=r'C:\Users\IKIT-SILA\Desktop\Pr\fastml\\'+namefile))

	name_pred = str(result[1])
	name_pred = int(name_pred[name_pred.find('(')+1:name_pred.find(')')])
	perc_pred = str(result[2][name_pred])
	perc_pred = round(float(perc_pred[perc_pred.find('(')+1:perc_pred.find(')')]),2)

	if perc_pred >= 0.9:
		return {"material": result[0]}
	else:
		return {}
