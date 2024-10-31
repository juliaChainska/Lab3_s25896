import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV


df = pd.read_csv('/Users/juliachainska/Downloads/CollegeDistance.csv')
df = df.drop(columns=['rownames'])

#spawdzanie brakujących wartości (w tym zbiorze nie ma)
missing_values = df.isnull().sum()


# WYKRESY
# Histogram dla każdej zmiennej numerycznej
# df.hist(bins=15, figsize=(15, 10), layout=(3, 3))
# plt.suptitle("Histogramy zmiennych numerycznych")
# plt.show()

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
n_cols = len(numeric_cols)

n_rows = (n_cols + 2) // 3
fig, axes = plt.subplots(n_rows, 3, figsize=(15, 5 * n_rows))
axes = axes.flatten()

for i, col in enumerate(numeric_cols):
    sns.histplot(df[col], ax=axes[i], kde=True)
    axes[i].set_title(f'Histogram zmiennej {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Liczność')

for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

#Wykresy zmiennych kategorycznych
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
n_cols = len(categorical_cols)

n_rows = (n_cols + 2) // 3  #zaokrąglenie w górę jeśli mamy niepełne wiersze
fig, axes = plt.subplots(n_rows, 3, figsize=(15, 5 * n_rows))

axes = axes.flatten()

for i, col in enumerate(categorical_cols):
    sns.countplot(x=df[col], ax=axes[i])
    axes[i].set_title(f'Histogram zmiennych kategorycznych w {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Liczność')
    axes[i].tick_params(axis='x', rotation=45)  # Rotacja etykiet na osi x

#usunięcie pustych wykresów
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()


#zamiana plci na numeric
df = pd.get_dummies(df, drop_first=True)

# Macierz korelacji
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Macierz korelacji zmiennych")
plt.show()


#imputacja średnią dla kolumn numerycznych
df.fillna(df.mean(), inplace=True)

#standaryzacja danych
features = df.drop(columns=['score']).columns
scaler = StandardScaler()
df[features] = scaler.fit_transform((df[features]))


#podzial danych na zbior treningowy i testowy
X = df.drop(columns=['score'])
y = df['score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#random forest model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train) #trenowanie modelu

#ocena jakosci modelu
y_pred = model.predict(X_test) #predykcja na zbiorze testowym

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"R²: {r2}")


#optymalizacja uzywając GridSearch
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1, scoring='r2')
grid_search.fit(X_train, y_train)
print("Najlepsze parametry:", grid_search.best_params_)
print("Najlepszy wynik R² na walidacji krzyżowej:", grid_search.best_score_)

#najlepszy model
best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MAE (zoptymalizowany model): {mae}")
print(f"MSE (zoptymalizowany model): {mse}")
print(f"R² (zoptymalizowany model): {r2}")
