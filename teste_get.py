import requests

headers = {'Authorization': 'Token 7d44c6b9416238b4f06ae4953397f55e6d1e0e8c'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 3

# Testando se o título do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Crie APIs REST com Python e Django REST Framework'
