import pandas as pd
import requests
import base64

class ManipulaDados:
  def __init__(self, username):
    self.username = username
    self.access_token = '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'
    self.api_base_url = 'https://api.github.com'
    self.headers = {
      'Authorization': 'Bearer ' + self.access_token, 
      'X-GitHub-Api-Version': '2022-11-28'
    }

  def create_repository(self, name, description):
    data = {
      'name': name,
      'description': description,
      'private': False
    }
    response = requests.post(f"{self.api_base_url}/user/repos", json=data, headers=self.headers)
    print(f'status_code criação do repositório: {response.status_code}')

  def upload_file(self, repo_name, filename, path):
    with open(path, "rb") as file:
        file_content = file.read()
    encoded_content = base64.b64encode(file_content)

    url = f"{self.api_base_url}/repos/{self.username}/{repo_name}/contents/{filename}"
    data = {
      "message": "Adicionando um novo arquivo",
      "content": encoded_content.decode("utf-8")
    }
    response = requests.put(url, json=data, headers=self.headers)
    print(f'status_code upload do arquivo: {response.status_code}')

# Testes ...
repository = ManipulaDados('mkafonso')
response = repository.upload_file('linguagens-utilizadas', 'mkafonso.csv', 'dados/mkafonso.csv')
print(response)