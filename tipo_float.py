"""
Tipo Float
Tipo real, decimal
Casa decimais

OBS: O separados de casas decimais na programação é o ponto e não a vírgula.
"""
print("-------------------")
#Errado do ponmto de vista do Float, mas gera um tuple
valor = 1,44
print(valor)

#Ele retornará (1, 44) seria ume tuple
print(type(valor)) 
print("-------------------")
#Certo para o ponto de vista Float
valor = 1.44
print(valor)

#Ele retornará 1.44 um FLOAT 
print(type(valor))
print("-------------------")
#É possivel fazer dupla atribuição
valor1, valor2 = 1,44
print(valor1)
print(valor2)
print(type(valor1))
print(type(valor2))

print("-------------------")
#Podemos converter um FLOAT para um INT
res = int(valor) # o resultado vai ser 1 porque está convertendo para um númerio inteiro, acaba perdendo a precisão
print(res)
print(type(res))


