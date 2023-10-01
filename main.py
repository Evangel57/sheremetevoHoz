from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import random

app = FastAPI()

# Импорт подготовленного датасета
dataset = pd.read_csv('df_finish_all_attr.csv')
dataset = dataset[dataset.config > 0]

def get_actions(float, cortege):
    pred_open_terminal = 0
    pred_open_race = 0

    w_terminal = 0.001
    w_race = 0.003

    float = abs(float)
    while float > 0:
            
        if float - w_race > 0:
            float -= w_terminal
            pred_open_terminal += 1
            if pred_open_terminal - pred_open_race > random.choice([0,1,2,1,0,5]):
                float -= w_race
                pred_open_race += 1
        else:
            float -= w_race
            pred_open_race += 1

    return {"how_advice_open_terminal": pred_open_terminal, "how_advice_open_race": pred_open_race}

# Интерфейс получаемых данных
class Data(BaseModel):
    week_day: str
    hour: int
    minutes: int
    real_stress: float

@app.get('/')
def worked():
    return 'Server worked'

@app.post('/processing')
def processing(data: Data):
    # Добавляем для удобства сравнения при получении ответа
    res = {"real_stress": data.real_stress}
    # Среднее арифметическое  (наше математическое предсказание)
    rate_mean = dataset[(dataset.hour==data.hour) & (dataset.minute==data.minutes) & (dataset.day_of_the_week == data.week_day)].rate.mean() 
    res['my_pred_stress'] = rate_mean

    # Стандартное отклонение
    diff = dataset[(dataset.hour==data.hour) & (dataset.minute==data.minutes) & (dataset.day_of_the_week == data.week_day)].rate.std()

    # Если отклонение больше среднего абсолютного, то предупреждаем и в потенциале при помощи обучения нейронной сети на новых данных по загрузкам терминалов - можно получить советы как поступить
    if rate_mean + diff < data.real_stress:
        res['alarm'] = True
        res['action'] = get_actions(rate_mean + diff, (diff, data.real_stress))
    elif rate_mean - diff > data.real_stress:
        res['alarm'] = True
        res['action'] = get_actions(rate_mean - diff, (diff, data.real_stress))
    else:
        res['alarm'] = False

    

    return res