def arithmetic_formatter(lista):
    if len(lista) <= 5:
        for i in lista:
            operacion = i.split(' ')
            primer_operando = operacion[0]
            segundo_operando = operacion[2]
            operador = operacion[1]

            cantidad_digitos_primer_operando = len(primer_operando)
            cantidad_digitos_segundo_operando = len(segundo_operando)

            if operador == '+' or operador == '-':
                if primer_operando.isnumeric() or segundo_operando.isnumeric():
                    if (cantidad_digitos_primer_operando <= 4) and (cantidad_digitos_segundo_operando <= 4):
                        # En este punto, se han cumplido todos los requerimientos para que se convierta la shit.

                        if cantidad_digitos_primer_operando >= cantidad_digitos_segundo_operando:
                            largo_operador_mas_largo = cantidad_digitos_primer_operando
                        else:
                            largo_operador_mas_largo = cantidad_digitos_segundo_operando

                        largo_operador_mas_largo += 2

                        espacios_primera_linea = largo_operador_mas_largo - cantidad_digitos_primer_operando
                        espacios_segunda_linea = largo_operador_mas_largo - cantidad_digitos_segundo_operando - 1


                        primera_linea = ''
                        for i in range(espacios_primera_linea):
                            primera_linea += ' '
                        
                        primera_linea += primer_operando


                        segunda_linea = operador
                        for i in range(espacios_segunda_linea):
                            segunda_linea += ' '
                        
                        segunda_linea += segundo_operando

                        tercera_linea = ''
                        for i in range(largo_operador_mas_largo):
                            tercera_linea += '-'
                        
                        suma_operadores = int(primer_operando) + int(segundo_operando)
                        largo_suma = len(str(suma_operadores))
                        espacios_cuarta_linea = largo_operador_mas_largo - largo_suma

                        cuarta_linea = ''
                        for i in range(espacios_cuarta_linea):
                            cuarta_linea += ' '
                        
                        cuarta_linea += str(suma_operadores)
                        
                        todo = f'{primera_linea} \n {segunda_linea} \n {tercera_linea} \n {cuarta_linea}'

                        print(todo)
  
                    else:
                        print('Error: Numbers cannot be more than four digits.')
                else:
                    print('Error: Numbers must only contain digits.')
            else:
                print("Error: Operator must be '+' or '-'") 
    else:
        print('Error: Too many problems.')