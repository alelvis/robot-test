from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell_world():
  return "YoloSwag"

@app.route("/about")
def about():
  return "Alphonse e bonitao"

@app.route("/contact")
def contact():
  return "We here bro"
