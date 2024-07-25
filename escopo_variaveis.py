"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis gloabais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis locais;
    - Variáveis locais são reconhecida apenas no bloco onde foram declaradas, ou seja, seu escopo está limitando ao bloco onde foi declarada

Para declara as variáveis em python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declaramos uma variável, nos não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em JAVA
int numero = 15;
"""

numero = 15
print(numero)
print(type(numero))

#Exemplo de um escopo

if numero > 10:
    novonum = numero + 10 # A variavel 'novonum' está declarada localmente dentro do bloco do if. Portanto é local
    print(novonum)

