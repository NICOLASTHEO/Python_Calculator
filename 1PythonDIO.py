###  Pratice - basics skills ###
#   Introdução: IDE, integrate development environment= recursos que facilitam o desenvolvimento de aplicações.
# Exemplo de IDE: PyCharm e Visual Studio Code- VS Code


print('hello, world')

a= 10
b=5
soma=a+b
subtração=a-b
multiplicação=a*b
divisão=a/b   #só uma barra o resultado virá em FLOAT
divisão2=a//b  # result. em forma de INTEIRO
resto=a%b   #resto da divisão de a / b

print(soma)
print(subtração)
print(multiplicação)
print(divisão)
print(divisão2)
print(resto)

print(type(soma))

#float e inteiros não realizam calculos com strings, deve-se converter:
print('soma: ' + str(soma)) # o Python irá converter o int soma para str e irá concatenar. Result.--> soma: 16
print(int(divisão)) #converte float para int

x='1'
soma2= int(x)+1
print(soma2)

#para não ficar informando se é str, float, ou se int que serão convertidos, e o tipo do calculo (+, -, / ,*) usa-se o FORMAT
#O FORMAT é inteligente e se encarregará de descobrir os requisitos. Ex. FORMAT:
print("soma: {}" .format(soma))
print('soma2: {}' .format(soma2))
print('resto: {}' .format(resto))

print('os resultados são: soma: {} e subtração: {}' .format(soma, subtração))

# Outra forma: e tbm mudando a visualização com \n
print('os valores são: \n soma: {soma} \n subtração: {sub}'. format(soma=soma, sub=subtração))

print("soma: {soma} \nsubtração: {subtração}"
'\nmultiplicação: {multiplicação} \ndivisão: {divisão}'
'\nresto: {resto}'.format(soma=soma, subtração=subtração,
multiplicação=multiplicação, divisão=divisão,
resto=resto))
