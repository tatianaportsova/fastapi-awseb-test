from fastapi import FastAPI
from joblib import load
import pandas as pd

app = FastAPI()
pipeline = load('./pipeline.joblib')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/predict')
def predict(title: str):
    """
    Predict whether a news article is real or fake news, 
    based on its title.

    Naive baseline: Always predicts 'fake'
    """
    df = pd.DataFrame.from_dict({'title':[title]})
    pred = pipeline.predict(df)
    return{'prediction':pred[0]}