from fastapi import FastAPI, Header, Body
from fastapi.middleware.cors import CORSMiddleware
import assistants.chatBot as chatBot

# uvicorn main:app --port 8080

app = FastAPI()

@app.get("/chatAssistant/")
def chatAssistant(
    data: dict = Body(...)):
    
    mess = data.get("mess")
    system = data.get("system", "")
    history = data.get("history", [])

    respons = chatBot.chatAssistant(mess, system, history)
    return respons

@app.get("/chatContext/")
def chatContext(
    data: dict = Body(...)):
    
    mess = data.get("mess")
    system = data.get("system", "")
    history = data.get("history", [])

    respons = chatBot.chatContext(mess, system, history)
    return respons
