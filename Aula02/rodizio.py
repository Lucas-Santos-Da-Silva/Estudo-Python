print("Este programa analisa os valores digitados de 0 à 9 e diz se o veiculo cadastrado poderá rodar naquele dia")
digito = input ("Entre com um número de 0 à 9: ")
match digito:
    case '1' | '2':
        print ("O seu carro não poderá rodar em segunda-feira")
    case '3' | '4':
        print ("O seu carro não poderá rodar em terça-feira")
    case '5' | '6':
        print ("O seu carro não poderá rodar em quarta-feira")
    case '7' | '8':
        print ("O seu carro não poderá rodar em quinta-feira")
    case '9' | '0':
        print ("O seu carro não poderá rodar em sexta-feira")
    case _:
        print("Valor incorreto. Tente outra vez")