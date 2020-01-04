# python-alelo

![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/ricardochaves/python-alelo/Build/master) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/2aed0b458670411c800954bcce1ab8e6)](https://www.codacy.com/manual/ricardochaves/python-alelo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ricardochaves/python-alelo&amp;utm_campaign=Badge_Coverage) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/2aed0b458670411c800954bcce1ab8e6)](https://www.codacy.com/manual/ricardochaves/python-alelo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ricardochaves/python-alelo&amp;utm_campaign=Badge_Grade) [![Updates](https://pyup.io/repos/github/ricardochaves/python-alelo/shield.svg)](https://pyup.io/repos/github/ricardochaves/python-alelo/) [![Python 3](https://pyup.io/repos/github/ricardochaves/python-alelo/python-3-shield.svg)](https://pyup.io/repos/github/ricardochaves/python-alelo/) [![Maintainability](https://api.codeclimate.com/v1/badges/0128ad980aa5f18fa280/maintainability)](https://codeclimate.com/github/ricardochaves/python-alelo/maintainability) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/ricardochaves/python-alelo/blob/master/LICENSE) [![PyPI version](https://badge.fury.io/py/python-alelo.svg)](https://badge.fury.io/py/python-alelo) [![Downloads](https://pepy.tech/badge/python-alelo/week)](https://pepy.tech/project/python-alelo/week) [![Downloads](https://pepy.tech/badge/python-alelo/month)](https://pepy.tech/project/python-alelo/month) [![Downloads](https://pepy.tech/badge/python-alelo)](https://pepy.tech/project/python-alelo)

---
A Alelo ainda não tem uma API para a gente pegar os nossos dados. Por isso fiz essa lib para poder melhorar o meu [financeiro-bot](https://github.com/ricardochaves/financeiro-bot)

Contribuições são bem vindas para colocar outros cartões.

## Como usar

Para instalar `pip install python-alelo`

```python
from python_alelo.alelo import Alelo
from python_alelo.alelo import Card
from typing import List

a = Alelo(cpf="SEU-CPF", pwd="SUA-SENHA")
a.login()

# Você precisa pegar os seus cartões para pegar o id deles
cards: List[Card] = a.get_cards()

# Pega o primeiro card
card: Card = cards[0]

# Pega todas as cinco últimas transações
print(a.get_transactions(card))

# Para pegar o saldo do cartão
s = a.get_statement(card.id)
print(s["statement"]["balance"])

```

O retorno do `get_transactions` é assim, esse é o retorno real do meu cartão:

```json
{
   "transactions":[
      {
         "date":"22/11",
         "value":5.1,
         "moneyType":"R$",
         "type":"DEBIT",
         "icon":"shopping",
         "description":"Pao To Go",
         "virtualCard":false
      },
      {
         "date":"15/11",
         "value":84,
         "moneyType":"R$",
         "type":"DEBIT",
         "icon":"shopping",
         "description":"VIA POMPEIA",
         "virtualCard":false
      },
      {
         "date":"14/11",
         "value":30,
         "moneyType":"R$",
         "type":"DEBIT",
         "icon":"shopping",
         "description":"T B B VILA OLIMPIA RES",
         "virtualCard":false
      },
      {
         "date":"11/11",
         "value":43.8,
         "moneyType":"R$",
         "type":"DEBIT",
         "icon":"shopping",
         "description":"KADALORA PIZZARIA",
         "virtualCard":false
      },
      {
         "date":"10/11",
         "value":5.9,
         "moneyType":"R$",
         "type":"DEBIT",
         "icon":"shopping",
         "description":"STARBUCKS 008-ELDORADO",
         "virtualCard":false
      }
   ],
   "average":33.76
}
```

## Opções

Para pegar mais transações vc pode fazer assim:

```python
from python_alelo.alelo import TransactionsTime

a.get_transactions(card, TransactionsTime.LAST_FIVE)
a.get_transactions(card, TransactionsTime.LAST_FIFTY_DAYS)
a.get_transactions(card, TransactionsTime.LAST_MONTH)
a.get_transactions(card, TransactionsTime.LAST_THREE_MONTHS)
a.get_transactions(card, TransactionsTime.LAST_FOUR_MONTHS)

```
