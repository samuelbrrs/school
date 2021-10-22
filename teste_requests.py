import requests


# GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
print(avaliacoes.status_code)

# Possibilidade além de ferramentas como o Insomnia
