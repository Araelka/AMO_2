import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train.values.ravel())

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)