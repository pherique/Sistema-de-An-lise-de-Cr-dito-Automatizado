#Esse arquivo vai simular a consulta dos dados de uma empresa usando o CNPJ.
#Na vida real, usaríamos uma API pública ou paga, mas aqui vamos simular os dados para o aprendizado.

import random # importamos a biblioteca random para gerar números aleatórios

def simular_dados_clientes(cpf):
    #simula uma consulta de dados de CPFs
    nomes_ficticios = [
        "Joao", "Ana", "Cicera", "Pedro", "Carlos", "Maria", "Fernanda", "Lucas", "Julia", "Roberto"
    ]
    return {
        'cpf': cpf,
        'nome': random.choice(nomes_ficticios),  # escolhe um nome aleatório da lista
        'score': random.randint(300, 850),  # gera um score de crédito aleatório entre 300 e 850
        'dividas': random.randint(0, 10000),  # gera um valor de dívidas aleatório entre 0 e 10.000
        'rendas': random.randint(1000, 5000)  # gera uma renda mensal aleatória entre 1.000 e 5.000
        
    }