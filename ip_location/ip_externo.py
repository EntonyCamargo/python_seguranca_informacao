import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']
loc = dados['loc']

print('Detalhes do IP externo\n')
print('lo: {5}\nIP: {4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg: {0}'.format(org, regiao, pais, cid, ip, loc))