from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "n18"}

#@app.get("/knn")
#def read_item(w: float, l: float):
#    fish_class = knn_api(l, w)
#    result_msg = f"🐟 길이 {l}에 무게 {w}인 물고기는 {fish_class}로 예측됩니다!"
#    return {"result": result_msg}

@app.get("/food")
def food(name: str):
    # 현재 이곳에 들어오는 시간
    # 음식 이름과 시간을 csv 형태로 저장 -> 경로 : ~/code/data/food.csv
    return {"food": name, 'time' : '2024-09-12 11:12:13'} # return값은 아무렇게나 해도 됨
