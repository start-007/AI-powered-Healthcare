
from flask import Flask,render_template,request,jsonify

from chat import response 
from diseaseDetectTest import predictDisease
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import folium


app=Flask(__name__)

API_KEY="AIzaSyBymMj3USLsqETLF97WrBFagi7jEdL5SpM"
GoogleMaps(app,key=API_KEY)


@app.get("/login")
def loginpage():
  return render_template("login.html")


@app.get("/signup")
def loginpage():
  return render_template("signup.html")


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


@app.route("/maps")
def mapview():
    # we add some marker here
  map = folium.Map(
      location=[20.5937, 78.9629],
      tiles='Stamen Terrain',
      zoom_start=12
  )

  folium.Marker(
      location=[15.3181, 78.2255],
      popup="<b>Marker 3 here</b>",
      tooltip="Click Here!",
      icon=folium.Icon(color='red')
  ).add_to(map)

  return map._repr_html_()

if __name__ == '__main__':
  app.run(debug=True)

