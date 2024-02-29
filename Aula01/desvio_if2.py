n1 = input ("Digite a primeira nota do aluno: ")
n2 = input ("Digite a segunda nota do aluno: ")
n3 = input ("Digite a terceira nota do aluno: ")
n4 = input ("Digite a quarto nota do aluno: ")
rs = int(n1)+int(n2)+int(n3)+int(n4) / 4
print ("A sua média é: ",rs,", então você está")
if (rs>= 7):
    print("Aprovado")
elif (rs<= 4):
    print("Recuperação")
else:
    print("Recuperação")
#Se o aluno tiver uma média acima ou igual a 7,
#então estará APROVADO, Senão se a média
#for abaixo ou igual a 4, então estará REPROVADO
#caso contrário, estará em RECUPERAÇÃO