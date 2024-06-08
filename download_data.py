import requests
import zipfile
import io

def download_data(url, output_path):
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as zfile:
        zfile.extractall(output_path)

download_data('https://github.com/user/repo/archive/refs/heads/main.zip', 'data/')