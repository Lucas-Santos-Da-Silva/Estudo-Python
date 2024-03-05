#Criar uma função que escreve a tabuada para um determinado 
#Valor definido pelo usuário em um arquivo de texto

def montar_tabuada(numero=0):
    print("Escreva um num")
    arq = open ("tabuada.txt","a")
    for i in range(1,11):
        arq.write(str(numero) + "x" + str(i) + " = " + str(numero*i)+"\n")
    arq.close()
n = input("Digite um número: ")
montar_tabuada(int(n))
