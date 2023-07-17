# linguagens-utilizadas
Repositorio com as linguagens de prog da Amazon

### gerar o dataframe com as linguagens mais utilizadas no repositório `mkafonso`
```
mkafonso = DadosRepositorios('mkafonso')
response = mkafonso.generate_df('mkafonso')
print(response)
```

### enviar os dados no repositório automaticamente (o token expira em 30 dias)
```
repository = ManipulaDados('mkafonso')
response = repository.upload_file('linguagens-utilizadas', 'mkafonso.csv', 'dados/mkafonso.csv')
print(response)
```
