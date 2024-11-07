import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib

# Ładowanie danych z repozytorium Lab3
data = pd.read_csv('CollegeDistance.csv')
# url = "https://raw.githubusercontent.com/juliaChainska/Lab3_s25896/refs/heads/main/CollegeDistance.csv"
# data = pd.read_csv(url)

# Kolumny kategoryczne
label_encoders = {}
for column in ['gender', 'ethnicity', 'fcollege', 'mcollege', 'home', 'urban', 'region']:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])

X = data[['fcollege', 'mcollege', 'home', 'urban', 'unemp', 'wage', 'distance', 'tuition', 'education', 'region']]
y = data['score']

# Podział na dane treningowe i testowe
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Trenowanie modelu
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Zapis modelu i labeli
joblib.dump(model, 'model.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')
print("Model i kodery etykiet zostały zapisane.")