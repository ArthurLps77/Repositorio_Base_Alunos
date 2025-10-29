import requests

#definir o nome para consulta
nome = input('Digite o nome da pessoa ').strip()

#url da api
url = f'https://api.agify.io/?name={nome}'

#fazer requisisão
response = requests.get(url)

#processar resposta
if response.status_code ==200:
    dados = response.json()
    print(f'Nome:{dados['name']}')
    print(f'Idade estimada:{dados['age']}anos')
    print(f'Numero de registros analisados:{dados['age']}anos')
else:
    print(f'Erro ao acessar a API:{response.status_code}')