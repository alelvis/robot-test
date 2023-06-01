from flask import Flask

app = Flask(__name__)

@app.routes("/")
def hell_world():
  return "YoloSwag"
