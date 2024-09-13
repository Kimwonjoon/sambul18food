from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import time
import pandas as pd

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8899",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    ts = time.strftime('%Y-%m-%d %H:%M:%S')

    # 음식 이름과 시간을 csv 형태로 저장 -> 경로 : ~/code/data/food.csv
    path = "/code/data/food.csv"
    if os.path.exists(path): # 파일이 이미 있다면
        data = pd.read_csv(path)
        df = pd.DataFrame({'time' : [ts], 'food' : [name]})
        new_df = pd.concat([data, df], ignore_index = True)
        new_df.to_csv(path, index = False)
    else: # 없다면
        os.makedirs(os.path.dirname(path), exist_ok=True)
        df = pd.DataFrame({'time' : [ts], 'food' : [name]})
        df.to_csv(path, index = False)

    return {'time' : ts, 'food' : name} # return값은 아무렇게나 해도 됨
