"""
Tipo booleano

2 Constante, Verdadeiro ou falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula 

"""
print("-------------------")
ativo = True
print(ativo)

"""
Operação básica

#Negação (not):

Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro

"""
print("-------------------")
print(not ativo)
logado = False

# Ou (or):
"""
É uma operação binária, ou seja, depedende de dois valores, Ou um ou outro deve ser verdadeiro.
True or True = True
True or False = True
"""
print("-------------------")
print(ativo or logado)

# E (and):

"""
Também uma operação binária, ou seja, depedende de dopis valores. Ambos os valores devem ser verdadeiro.
mesmo se False e False ele retonará falso também, apenas o resultado de True e True retornará o valor verdadeiro.
"""
print("-------------------")
ativo = True
logado = True
print(ativo and logado)

