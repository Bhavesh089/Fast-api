  # Server
import uvicorn
from fastapi import FastAPI
import json

# Data Handling
from pydantic import BaseModel

app = FastAPI()


@app.post("/body")
def someMethod(body: dict):
    fileName = 'Response_data.json'
    with open(fileName, "w+") as write_file:
        json.dump(body,write_file)
    return body

@app.get("/readingfile")
def ReadingJson():
 with open('Response_data.json') as f:
  data = json.load(f)
    return data    

@app.get("/")
def hello():
    return {"message":"How are you"}
