#Esse arquivo vai analisar os dados simulados de cada empresa e dizer se ela tem risco BAIXO, MÉDIO ou ALTO com base em regras simples.


def avliar_credito(dados):
    renda = dados.get('rendas', 0)  # obtém a renda do cliente, ou 0 se não estiver presente
    score = dados.get('score', 0)  # obtém o score do cliente, ou 0 se não estiver presente
    dividas = dados.get('dividas', 0)  # obtém as dívidas do cliente, ou 0 se não estiver presente
    
    # Regras simples para avaliar o risco de crédito
    if score >= 700 and renda > 2000 and dividas < 5000:
        return 'BAIXO'  # risco baixo se o score for alto, renda for boa e dívidas forem baixas
    elif score >= 500 and renda > 1000 and dividas < 10000:
        return 'MÉDIO'  # risco médio se o score for razoável, renda for média e dívidas forem moderadas
    else:
        return 'ALTO'  # risco alto se nenhuma das condições acima for atendida