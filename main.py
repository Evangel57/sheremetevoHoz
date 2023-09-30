from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def worked():
    return 'Server worked'

class Data(BaseModel):
    week_day: str
    hour: int
    minutes: int
    pred_stress: float

@app.post('/processing')
def processing(data: Data):
    return data