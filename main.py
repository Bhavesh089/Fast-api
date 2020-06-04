  
from fastapi import FastAPI

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"message":"Hello TutLinks.com"}




# # Server
# import uvicorn
# from fastapi import FastAPI
# import json

# # Data Handling
# from pydantic import BaseModel

# app = FastAPI()


# @app.post("/body")
# def someMethod(body: dict):
#     fileName = 'Response_data.json'
#     with open(fileName, "w+") as write_file:
#         json.dump(body,write_file)
#     return fileName

# @app.get("/")
# def hello():
#     return {"message":"Hello TutLinks.com"}