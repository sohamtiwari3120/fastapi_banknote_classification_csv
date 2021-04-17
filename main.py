from fastapi import FastAPI, File, HTTPException
from fastapi.datastructures import UploadFile
from pydantic import BaseModel


import uvicorn
import pandas as pd
import numpy as np
import pickle

class PredictInput(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float


app = FastAPI()
pickle_in = open('./classifier.pkl', 'rb')
clf = pickle.load(pickle_in)

def make_pred(variance, skewness, curtosis, entropy):
    """a simple function to return only the prediction

    Parameters
    ----------
    variance : float
        variance of note
    skewness : float
        skewness input
    curtosis : float
        curtosis input
    entropy : float
        entropy input

    Returns
    -------
    int
        predicted value 1 - authentic, 0 - unauthentic
    """
    return clf.predict(np.array([variance, skewness, curtosis, entropy]).reshape(1, -1))

@app.get('/')
async def root():
    return {
        "message": "Hello, world!"
    }


@app.post('/predict')
def predict_note_authentication(input: PredictInput):
    """Predict if note is authentic

    Parameters
    ----------
    input : PredictInput
        dict {
          "variance": 0,
          "skewness": 0,
          "curtosis": 0,
          "entropy": 0
        }

    Returns
    -------
    str
        string containing prediction result
    """
    prediction = make_pred(input.variance, input.skewness, input.curtosis, input.entropy)
    return f'The prediction value is {prediction}'


@app.post('/predictFile')
async def predict_note_authentication_csv_file(file: UploadFile = File(...)):
    """Generate predictions for CSV file containing the values for variance, skewness, curtosis, entropy. Header line in CSV may or may not be present.

    Parameters
    ----------
    file : UploadFile, optional
        CSV file to be uploaded in form data, by default File(...)

    Returns
    -------
    dict
        dict containing key 'predictions' and having value as the list of predictions for all the inputs provided in the csv file

    Raises
    ------
    HTTPException
        returns 500 server error whenever there is any problem while processing input file or making predictions.
    """
    byte_contents = await file.read()
    data_list = []
    for i in byte_contents.decode('utf-8').splitlines():
        vals = i.split(',')
        try:
            vals = list(map(lambda s: float(s), vals))
            data_list += [vals]
        except Exception as e:
            print(e)
    try:
        preds = clf.predict(np.array(data_list))
        return {
            'predictions': preds.tolist()
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f'Error in processing uploading csv file.\n{e}')



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
