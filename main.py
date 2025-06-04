from src.analisador import analisador #estamos chamando uma função que ainda vamos criar, que será responsável por ler o CSV, consultar os dados e gerar o relatório.

if __name__ == "__main__": # isso significa "se este for o arquivo principal, execute o que está abaixo"
    caminho_csv = "dados/dados.csv" # aqui estamos definindo o caminho do arquivo CSV que vamos analisar
    relatorio = analisador(caminho_csv) # chamamos a função analisador, passando o caminho do CSV, e armazenamos o resultado na variável relatorio