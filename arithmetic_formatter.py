def arithmetic_formatter(lista):
    if len(lista) <= 5:
        for i in lista:
            operacion = i.split(' ')

            if operacion[1] == '+' or operacion[1] == '-':
                if operacion[0].isnum() or operacion[2].isnum():
                    if (len(operacion[0]) <= 4) and (len(operacion[2]) <= 4):
                        # En este punto, se han cumplido todos los requerimientos para que se convierta la shit.
                    
                    else:
                        print('Error: Numbers cannot be more than four digits.')
                else:
                    print('Error: Numbers must only contain digits.')
            else:
                print("Error: Operator must be '+' or '-'") 
    else:
        print('Error: Too many problems.')