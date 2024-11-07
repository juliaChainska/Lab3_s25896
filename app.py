from flask import Flask, request, jsonify
import pandas as pd
import joblib

# Inicjalizacja aplikacji Flask
app = Flask(__name__)

# Ładowanie modelu
model = joblib.load('model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

# Endpoint do przewidywania
@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    input_df = pd.DataFrame(input_data)

    for column in ['gender', 'ethnicity', 'fcollege', 'mcollege', 'home', 'urban', 'region']:
        if column in input_df.columns:
            input_df[column] = label_encoders[column].transform(input_df[column])

    # Przewidywanie
    predictions = model.predict(input_df)

    # Wynik przewidywania
    return jsonify({'predictions': predictions.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
