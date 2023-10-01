
<h1 align="center">Шереметьево</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>

**Запуск модуля:**
===================
1. git clone https://github.com/Evangel57/sheremetevoHoz.git клонируем репозиторий
2. В терминале: pipenv shell (Иницилизируем виртуальную среду)
3. В терминале: uvicorn main:app --reload (Запуск сервера локально)

___Использование:___
Отправляем post запрос в формате


    "week_day": str (день недели)
    "hour": int (час)
    "minutes": int (минуты)
    "real_stress": float (нагрузка)
    
 

Получаем ответ в формате


    "real_stress": float, (нагрузка)
    "my_pred_stress": float, (прадсказанная нагрузка)
    "alarm": bool, (предупреждение есть ли отклонения в нагрузке)
    "action": { (если есть отклонения в нагрузке, то отправляем данный параметр)
        "how_advice_open_terminal": int, (сколько рекомендуем открыть терминалов)
        "how_advice_open_race": int (сколько рекомендуем добавить рейсов)
    }
    


**КАК ПОЛУЧАЕМ ОТКЛОНЕНИЕ:**
Находим разницу между нашим предсказанием и стандартным отклонением (std) и если


    "my_pred_stress + std < real_stress"
    "my_pred_stress - std > real_stress"


то отклонение серьезное

Пример:
======

отправили


    "week_day": "Monday",
    "hour": 21,
    "minutes": 45,
    "real_stress": 0.1
    


получили


    "real_stress": 0.1,
    "my_pred_stress": 0.004044663807045383,
    "alarm": true,
    "action": {
        "how_advice_open_terminal": 4,
        "how_advice_open_race": 4
    }
    
