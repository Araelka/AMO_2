import os
import pandas as pd
import requests

# Создание папки data, если она не существует
if not os.path.exists('data'):
    os.makedirs('data')

# Функция для загрузки данных
def download_data(url, output_path):
    response = requests.get(url)
    with open(output_path, 'wb') as f:
        f.write(response.content)

# URL репозитория и путь для сохранения данных
github_url = 'https://github.com/gainadir12/Diabet/raw/main/Diabetes.csv'
output_path = 'data/Diabetes.csv'

# Загрузка данных
download_data(github_url, output_path)

# Чтение данных в DataFrame
data = pd.read_csv(output_path)

# Очистка данных (если необходимо)
# Например, удаление строк с пропущенными значениями
cleaned_data = data.dropna()

# Сохранение очищенных данных
cleaned_data.to_csv('data/cleaned_diabetes_data.csv', index=False)