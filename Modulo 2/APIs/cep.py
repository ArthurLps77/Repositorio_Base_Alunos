# Crie uma API que consulte o CEP e informe o endereço

# Importamos a biblioteca requests
import requests

# Usuário informa o CEP que deseja consultar
cep = input('Digite o CEP (somente números): ')

# Indicamos a URL da API (corrigido: adicionada a barra após /ws/)
url = f'https://viacep.com.br/ws/{cep}/json/'

# Fazemos a requisição
resposta = requests.get(url)

# Verificamos se a requisição foi bem-sucedida
if resposta.status_code == 200:
    dados = resposta.json()
    
    if 'erro' not in dados:
        print(f"\nCEP: {dados['cep']}")
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
    else:
        print('CEP não encontrado.')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)