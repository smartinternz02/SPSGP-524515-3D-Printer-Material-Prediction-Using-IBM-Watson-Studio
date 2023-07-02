from flask import Flask, render_template, request, jsonify, render_template
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open("printer.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    # columns = ['abs','pla']
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    if prediction == 0:
        material_type = "ABS"
    elif prediction == 1:
        material_type = "PLA"
    else:
        material_type = "Unknown"
    prediction_text = "The Material type is {}".format(material_type)
    return render_template("index.html", prediction_text = prediction_text)

# scaler = pickle.load(open('static/scaler.pkl', 'rb'))
if __name__ == '__main__':
    app.run(debug=True)


