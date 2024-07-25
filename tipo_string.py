"""
Tipo String

Em python, um dado é considero do tipo string sempre que estiver entre aspas simples, duplas, Simples triplas e duplas triplas
Exemplo:
'uma string','234','true', '42.3' -> Aspas simples 
"123", "Outra string", "false", "10.5" -> Aspas duplas
'''567''','''String diferente''', '''true''', '''50.01''' -> Aspas simples triplas
"""
nome = 'Lucas'
sobrenome = "Marques"
idade = '''22''' #Não colocar idade como uma STRING usando so apenas como um exemplo

print(nome, sobrenome, idade)
print(type(nome))
print(type(sobrenome))
print(type(idade))
print('--------------')
print(nome.upper()) #Utilizando o UPPER para deixa a STRING em maiusculo
print(nome.lower()) #Utilizando o LOWER para deixa a STRING em minisculo
nome = "Lucas Marques"
print(nome.split()) #Utilizando o SPLIT para transforma a STRING e uma list
print('--------------')
print(nome[0:5])#Selecionando o começo e fim das letra da string conhecemos por Slice String
print(nome[6:13])#Um segunda forma de fazer o Slice string
print('--------------')
print(nome.split()[0]) #Utilizando o split para transforma em uma List e usando a posição [0] para indetificar como o primeiro elemento da List
print('--------------')
print(nome[::-1]) # -> Comece do primeiro elemento, vá até o ultimo elemento e inverta
print('--------------')
print(nome.replace('c',"k")) #Substitua a Letra (C pelo K) o replace da letra tem que estar da mesma forma que na String 
