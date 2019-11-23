# python-alelo

A Alelo ainda não tem uma API para a gente pegar os nossos dados. Por isso fiz essa lib para poder melhorar o meu [financeiro-bot](https://github.com/ricardochaves/financeiro-bot)

Funciona apenas com vale refeição Alelo, esse é o único cartão que eu tenho. 

Contribuições são bem vindas para colocar outros cartões.

## Como usar

Para instalar `pip install python-alelo`


```python
from python_alelo.alelo import Alelo

a = Alelo(cpf="SEU-CPF", pwd="SUA-SENHA")
a.login()

# Você precisa pegar os seus cartões para pegar o id deles
cards = a.get_cards()

# Pega o id do card que vc quser na lista
id = cards[0]["id"]

# Pega todas as cinco últimas transações
print(a.get_transactions(id))

# Para pegar o saldo do cartão
s = a.get_statement(id)
print(s["statement"]["balance"])

```

O retorno do `get_transactions` é assim, esse é o retorno real do meu cartão:

```json
{'transactions': [{'date': '22/11', 'value': 5.1, 'moneyType': 'R$', 'type': 'DEBIT', 'icon': 'shopping', 'description': 'Pao To Go', 'virtualCard': False}, {'date': '15/11', 'value': 84, 'moneyType': 'R$', 'type': 'DEBIT', 'icon': 'shopping', 'description': 'VIA POMPEIA', 'virtualCard': False}, {'date': '14/11', 'value': 30, 'moneyType': 'R$', 'type': 'DEBIT', 'icon': 'shopping', 'description': 'T B B VILA OLIMPIA RES', 'virtualCard': False}, {'date': '11/11', 'value': 43.8, 'moneyType': 'R$', 'type': 'DEBIT', 'icon': 'shopping', 'description': 'KADALORA PIZZARIA', 'virtualCard': False}, {'date': '10/11', 'value': 5.9, 'moneyType': 'R$', 'type': 'DEBIT', 'icon': 'shopping', 'description': 'STARBUCKS 008-ELDORADO', 'virtualCard': False}], 'average': 33.76}
```

## Opções

Para pegar mais transações vc pode fazer assim:

```python
from python_alelo.alelo import TransactionsTime

a.get_transactions(id, TransactionsTime.LAST_FIVE)
a.get_transactions(id, TransactionsTime.LAST_FIFTY_DAYS)
a.get_transactions(id, TransactionsTime.LAST_MONTH)
a.get_transactions(id, TransactionsTime.LAST_THREE_MONTHS)
a.get_transactions(id, TransactionsTime.LAST_FOUR_MONTHS)

```
