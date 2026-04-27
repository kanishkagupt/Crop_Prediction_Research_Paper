from flask import Flask, request, render_template, jsonify
import joblib

app = Flask(__name__)

# Load your machine learning model
model = joblib.load('crop_model')

# Crop Prediction Function
def predict_crop(input_features):
    prediction = model.predict([input_features])
    return prediction[0]

# Home Page – Crop Prediction Form
@app.route('/')
def home():
    return render_template('crop_pred.html')

# Crop Prediction from JSON Request (used by frontend JS)
@app.route('/results', methods=["POST"])
def get_prediction():
    if request.method == "POST":
        data = request.get_json()
        N = float(data['nitrogen'])
        P = float(data['phosphorous'])
        K = float(data['potassium'])
        temperature = float(data['temperature'])
        humidity = float(data['humidity'])
        ph = float(data['ph'])
        rainfall = float(data['rainfall'])

        input_features = [N, P, K, temperature, humidity, ph, rainfall]
        predicted_crop = predict_crop(input_features)

        return jsonify({'prediction': predicted_crop})


# Fertilizer Recommendation Page (Form + Logic)
@app.route('/fertilizer-recommendation', methods=['GET', 'POST'])
def fertilizer_recommendation():
    recommendation = None

    if request.method == 'POST':
        try:
            n = int(request.form['nitrogen'])
            p = int(request.form['phosphorus'])
            k = int(request.form['potassium'])

            recommendation_list = []

            if n < 50:
                recommendation_list.append("Apply Urea or Compost for Nitrogen.")
            elif n > 200:
                recommendation_list.append("Reduce nitrogen fertilizers to avoid toxicity.")

            if p < 50:
                recommendation_list.append("Add Single Super Phosphate or Bone Meal for Phosphorus.")
            elif p > 150:
                recommendation_list.append("Phosphorus is high. Avoid adding more.")

            if k < 50:
                recommendation_list.append("Use Muriate of Potash or Banana Peels for Potassium.")
            elif k > 150:
                recommendation_list.append("Potassium is sufficient. No extra needed.")

            recommendation = "<br>".join(recommendation_list)

        except ValueError:
            recommendation = "Please enter valid numeric values for N, P, and K."

    return render_template('fertilizer.html', recommendation=recommendation)



if __name__ == "__main__":
    app.run(debug=True)
