#Lê o arquivo CSV com os CPFs
#Consulta os dados do CNPJ (simulado por enquanto)
#Aplica regras de risco
#Gera um relatório simples


import os  #importa a biblioteca OS, usada para manipular arquivos e diretórios.
print(os.getcwd())  # Mostra onde o Python está procurando o arquivo
import pandas as pd #importa a biblioteca Pandas, usada para ler e gravar planilhas (CSV).
from src.simular_dados import simular_dados_clientes #importa a função simular_dados_cliente do módulo simular_dados, que gera dados fictícios de clientes.
from src.regras_credito import avliar_credito #importa o módulo regras_credito, que contém as regras de crédito a serem aplicadas.

def analisador(caminho_csv):
    # 1. Lê o arquivo CSV com os CPFs
    df = pd.read_csv(caminho_csv)  #lê o arquivo CSV e armazena os dados em um DataFrame do Pandas.
    
    resultados = []  #cria uma lista vazia para armazenar os resultados da análise.
    
    for cpf in df['CPF']:
        # 2. Consulta os dados do CPF (simulado por enquanto)
      print(f"Consultando dados para o CPF: {cpf}")  #imprime uma mensagem indicando que está consultando os dados do CPF.
      
      dados = simular_dados_clientes(cpf)  #chama a função simular_dados_cliente passando o CPF, que 
      risco = avliar_credito(dados)  #chama a função avliar_credito passando os dados do cliente, que retorna o risco associado ao CPF.
      
        resultados.append({
        'CPF': cpf,  # adiciona um dicionário com o CPF e o risco à lista de resultado
        'Risco': dados.get('cfp'),  # adiciona o risco associado ao CPF
        'Score': dados.get('score'),  # adiciona o score do cliente, se disponível
        'Dividas': dados.get('dividas'),  # adiciona as dívidas do cliente, se disponível
        'Rendas': dados.get('rendas')  # adiciona as rendas do cliente, se disponível
        })  # adiciona um dicionário com os resultados da análise à lista de resultados 
      
      # 3. Converter os resultados em um DataFrame
    df_resultado = pd.DataFrame(resultados)  #converte a lista de resultados em um DataFrame do Pandas.
    
    # 4. Garante que a pasta do relatório exista
    os.makedirs('relatorios', exist_ok=True)  #cria a pasta 'relatorios' se ela não existir, para armazenar o relatório.
        
    # 5. Salva o relatório em um arquivo CSV
    df_resultado.to_csv('relatorios/relatorio.csv', index=False)  #salva o DataFrame como um arquivo CSV na pasta 'relatorios', sem incluir o índice.
    print("Relatório gerado com sucesso!")  #imprime uma mensagem indicando que o relatório foi gerado com sucesso.
