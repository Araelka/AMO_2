# Загрузка данных
from sklearn.datasets import load_breast_cancer
import pandas as pd

# Загрузка набора данных
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Сохранение данных в CSV для использования в Jenkins
df.to_csv('breast_cancer_data.csv', index=False)
