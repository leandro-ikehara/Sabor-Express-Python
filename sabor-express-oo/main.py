from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint de abertura
    '''
    return {'Hello': 'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint de cardápio de restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        # dados_restaurante = {}
        dados_restaurante = []
        for item in dados_json:
            # nome_restaurante = item['Company']
            if item['Company'] == restaurante:
            # if nome_restaurante not in dados_restaurante:
            #     dados_restaurante[nome_restaurante] = []
            #     dados_restaurante[nome_restaurante].append({
                dados_restaurante.append({
                    "item": item['Item'],
                    "preço": item['price'],
                    "descrição": item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio':dados_restaurante}

        # print(dados_restaurante['McDonald’s'])
    else:
        # print(f'O erro foi {response.status_code}')
        return {'Erro': f'{response.status_code} - {response.text}'}