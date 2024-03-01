print("Este programa analisa os valores digitados de 0 à 6 e diz o dia da semana")
digito = input ("Entre com um número de 0 à 6: ")
match digito:
    case '0':
        print ("Domingo")
    case '1':
        print ("Segunda-feira")
    case '2':
        print ("Terça-feira")
    case '3':
        print ("Quarta-feira")
    case '4':
        print ("Quinta-feira")
    case '5':
        print ("Sexta-feira")
    case '6':
        print ("Sabado")
    case _:
        print("Valor incorreto. Tente outra vez")