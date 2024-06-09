import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Загрузка данных
data = pd.read_csv('processed_data.csv')

# Разделение данных
X = data.drop('target', axis=1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Сохранение модели
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)