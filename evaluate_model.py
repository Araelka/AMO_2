import pandas as pd
from sklearn.metrics import classification_report
import pickle

X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv('y_test.csv')

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

predictions = model.predict(X_test)

print(classification_report(y_test, predictions))