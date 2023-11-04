import pymongo
import random
from pydantic import BaseModel
import json
import time

myclient = pymongo.MongoClient("mongodb+srv://iot:iot@cluster0.ftx0nvn.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["Mydata"]
mycol = mydb["sensordata"]

def GetData():
    return random.randint(0,99)

def PostData(temp, humi):
    mydict = {
        "temp": temp,
        "humi": humi
    }
    print(mydict)
    mycol.insert_one(mydict)
    return "OK"

while True:
    data_temp = GetData()
    data_humi = GetData()

    print(PostData(data_temp, data_humi))

    time.sleep(50)