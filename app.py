from flask import Flask,request,jsonify
from flask_cors import CORS
from ai_generator import generate_business

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return "AI Business Generator Running"


@app.route("/generate",methods=["POST"])
def generate():

    data=request.json

    result=generate_business(data)

    return jsonify(result)



if __name__=="__main__":
    app.run(debug=True)
