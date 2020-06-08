from fastapi import FastAPI

app = FastAPI()


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
    return {'prediction': 'fake'}