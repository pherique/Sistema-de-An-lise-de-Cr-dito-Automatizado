import zipfile
import pandas as pd

# Criar DataFrame com os CPFs
data = {'CPF': [
    '12345678900',
    '98765432100',
    '11122233344',
    '99988877766',
    '55544433322',
    '90556658434',
    '47647585800'
]}

df = pd.DataFrame(data)

# Salvar como CSV
df.to_csv('dados.csv', index=False)

# Zipar o arquivo CSV
with zipfile.ZipFile('dados.zip', 'w') as zipf:
    zipf.write('dados.csv', arcname='dados.csv')
    
print("Arquivo CSV criado e compactado com sucesso em 'dados.zip'.")