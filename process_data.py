import pandas as pd

# Загрузка данных
data = pd.read_csv('Diabet-main/data.csv')

# Обработка данных (пример)
data['new_feature'] = data['feature1'] / data['feature2']

# Сохранение обработанных данных
data.to_csv('processed_data.csv', index=False)