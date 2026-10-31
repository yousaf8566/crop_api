from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    d = request.get_json()
    vals = [[d["N"], d["P"], d["K"], d["temperature"],
             d["humidity"], d["ph"], d["rainfall"]]]
    return jsonify({"crop": str(model.predict(vals)[0])})

@app.route("/")
def home():
    return "Crop API chal rahi hai"