import pandas as pd
import requests

class DadosRepositorios:
  def __init__(self, owner):
    self.owner = owner
    self.access_token = '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'
    self.api_base_url = 'https://api.github.com'
    self.headers = {
      'Authorization': 'Bearer ' + self.access_token, 
      'X-GitHub-Api-Version': '2022-11-28'
    }

  def fetch_repositories(self):
    repos_list = []
    for page_num in range(1, 20):
        try:
            url_page = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
            response = requests.get(url_page, headers=self.headers)
            repos_list.append(response.json())
        except:
            repos_list.append(None)
    return repos_list

  def fetch_repo_names(self, repos_list):
    repos_names = []
    for page in repos_list:
      for repo in page:
        try:
          repos_names.append(repo["name"])
        except:
            pass
    return repos_names
  
  def fetch_repo_languages(self, repos_list):
    repos_languages = []
    for page in repos_list:
      for repo in page:
        try:
          repos_languages.append(repo["language"])
        except:
            pass
    return repos_languages

  def generate_df(self):
    repositories = self.fetch_repositories()
    names = self.fetch_repo_names(repositories)
    languages = self.fetch_repo_languages(repositories)

    df = pd.DataFrame()
    df['repository_name'] = names
    df['language'] = languages
    return df

# Testes ...
mkafonso = DadosRepositorios('mkafonso')
response = mkafonso.generate_df()
print(response)