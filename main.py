import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import pymongo

app = FastAPI()

myclient = pymongo.MongoClient("mongodb+srv://iot:iot@cluster0.ftx0nvn.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["Mydata"]
mycol = mydb["sensordata"]
id = 0

class Item(BaseModel):
    data1: float
    data2: float

@app.get("/")
def root():
    return {"message": "Hello Word!"}

@app.get("/updates")
async def update_data(data1: float, data2: float):
    return {"temp: ": data1, "humi: ": data2}

@app.get("/get")
async def update_data():
    x = mycol.find_one()
    data_return = {
        "temp: ": x['temp'],
        "humi: ": x['humi']
    }
    print(data_return)
    return data_return

@app.post("/update_post")
async def update_data_post(item: Item):
    mydict = {
        "temp": int(item.data1),
        "humi": int(item.data2)
    }
    # print(mydict)
    mycol.insert_one(mydict)
    return "OK"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)