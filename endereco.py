import requests

cep = str(input('Qual é o seu CEP'))
endereco = 'https://viacep.com.br/ws/null/json/'
endereco=endereco.replace('null',cep)
print (endereco)
#print (type(endereco))
#print(endereco)
#print(len(endereco))
#endereco[4]=cep
#endereco.remove[4]
#print(endereco('4'))
#print (endereco[4])
#print(endereco)
#nend = str(endereco).strip('[]')
#str(nend).strip('''''')
#','.join(map(str,nend))
#print(nend)
response = requests.get(endereco)

print (response.json())
