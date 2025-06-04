
# 🧾 Analisador de Crédito - Pessoas Físicas (CPF)

Este projeto simula a análise de crédito de clientes pessoa física com base em seus CPFs. A proposta é ler um arquivo CSV contendo CPFs, simular dados financeiros fictícios e classificar o risco de crédito em **BAIXO**, **MÉDIO** ou **ALTO**.

## 📌 Funcionalidades
- Leitura de CPFs a partir de um arquivo CSV
- Geração simulada de dados: nome, renda, score e dívidas
- Avaliação de risco com base em regras simples
- Geração de relatório em CSV

## ▶️ Como executar

1. Instale o Python (versão 3.8+).
2. Instale o pacote `pandas`:
```bash
pip install pandas
```
3. Execute o script principal:
```bash
python main.py
```

## 📂 Estrutura
```
projeto/
├── main.py
├── analisador.py
├── src/
│   ├── simular_dados.py
│   └── regras_credito.py
├── dados/
│   └── clientes.csv
├── relatorios/
│   └── relatorio.csv
└── README.md
```

## ⚙️ Regras de Risco

- Score < 300 **OU** dívidas > R$ 3.000 → **ALTO**
- Renda < R$ 3.000 → **MÉDIO**
- Caso contrário → **BAIXO**

## 🛠 Tecnologias
- Python
- Pandas

## 📈 Objetivo
Este projeto foi criado com fins educacionais e como parte do meu aprendizado sobre análise de dados, simulação de APIs e aplicação de regras de negócio com Python.
