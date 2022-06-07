
from flask import Flask,render_template,request,jsonify

from chat import response 
from diseaseDetectTest import predictDisease
app=Flask(__name__)

@app.get("/")
def index_get():
  return render_template("index.html")

@app.get("/chatbot")
def chatbot_get():
  return render_template("chatbot.html")

@app.get("/voice-assistant")
def voicebot_get():
  return render_template("voiceAssistant.html")

@app.get("/detect-disease")
def diseaseDetect_get():
  return render_template("detectDisease.html")

@app.post("/predict")
def predict():
  text=request.get_json().get("message")
  print(text)
  res=response(text)
  message={"answer":res}
  return jsonify(message)

@app.post("/detect-disease")
def detectDisease():
  arr=request.get_json().get("message")
  result=predictDisease(arr)
  message={"answer":result}
  print(message)
  return jsonify(message)

  

