#Apresentaçao
'''
Criador: Thiago da Silva Moyses
Git: Thiago Moyses - https://github.com/thiagomoyses
Versão: 1.2
14/04/2020 - 15:08
'''
#bibliotecas
import requests
import json
import string
from hashlib import sha1
#Recebendo dados da API
urltoken = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=Seu Token')
#URL de envio
urlPost = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=Seu Token"
#alfabeto
alfaB = list(string.ascii_lowercase)
#Dicionario
urljson = urltoken.json()
#Decriptado
decript = ""
#campo cifrado
cesar = urljson['cifrado'].lower()
#Criando e alterando Json
def alterajson(apidict):
    with open("answer.json", "w") as filejson:
        json.dump(apidict, filejson)
#Chamando Funcao
alterajson(urljson)
#decriptando Cesar
for cont in cesar:
    if cont in alfaB:
        decript += alfaB[(alfaB.index(cont))-(urljson['numero_casas'])]
    else:
        decript += cont
#Atualizando dicionario
urljson['decifrado'] = decript
#crifrando em sha1
encriptSha1 = sha1(decript.encode())
urljson['resumo_criptografico'] = (encriptSha1.hexdigest())
alterajson(urljson)

#Enviando para a API
file = "C:\\Users\\thiag\\Desktop\\TI\\python\\CodeNation\\answer.json"
arquivo = {'answer': open(file,'rb')}

try:
    envia = requests.post(urlPost, files=arquivo)
    print(envia.text)
except ValueError:
    print(ValueError)