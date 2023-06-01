from flask import Flask

app = Flask(_name_)

@app.routes("/")
def hell_world():
  return "YoloSwag"
