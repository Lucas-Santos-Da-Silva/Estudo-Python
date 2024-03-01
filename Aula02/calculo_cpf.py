print("Programa que verifica se o CPF é válido")
cpf_usuario=input("Digite o seu CPF")
#esta variavel foi cirada oara calcular o peso de 10 até 2
peso10=10
#A variavel resultado guarda a soma da muiltiplicaçõpes
#entre os digitos do cpf e os pesos
resultado=0
#Para obter os 9 primeiros digitos do cpf foi necessário usar uma #estrutura for com uma contage de 0 até 9
for i in range(1,9):
    #exibindo um digito do cpf por vez em tela
    print(cpf_usuario[i])
    print(int(cpf_usuario[i])*peso10)
    #Para calcular um digito por vez com o peso foi
    #necessário converter cada digito em número inteiro
    #depois, somamos os resultados obtidos armazenando
    resultado+=int(cpf_usuario[i]*peso10)
    #Todas as vezes que o "laço" for rodar, será subtraido 
    #o valor 1 da variável peso10
    peso10-=1
    #Exibindo o resultado encontrado
print(resultado)
#A variável resto, guarda o resto da divisão
resto=resultado%11
#Se o resto da divisão for menor que 2, então o
#primeiro digito será 0(zero); Caso contrário o 
#devemos subtrair 11 pelo valor encontrado em resto
if (resto<2):
    print("Primeiro digito é 0")
else:
    print("Primeiro digito é"+str(11-resto))
