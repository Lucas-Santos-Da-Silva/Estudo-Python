#Pede um número e verifica se é par ou impar
numero = input ("Digite um número: ")
numero = int(numero)
if(numero % 2 == 0):
    print("O número digitado é par")
#É necessário realizar a conversão de texto para
#número, pois a função input sempre retorna o valor
#em formato texto. Então, utilizamos a função
#int para converter a vaiável número em valor
#numérico inteiro e assim realizar os cálculos necessários
else:
    print ("O número digitado é impar")
