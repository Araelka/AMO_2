import pandas as pd
from sklearn.metrics import accuracy_score
import pickle

# Загрузка данных
data = pd.read_csv('processed_data.csv')

# Разделение данных
X = data.drop('target', axis=1)
y = data['target']

# Загрузка модели
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Предсказание и оценка модели
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)

print(f"Model Accuracy: {accuracy:.2f}")