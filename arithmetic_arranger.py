def arithmetic_arranger(lista, resultados = False):
    if len(lista) <= 5:
        primeras_lineas = []
        segundas_lineas = []
        terceras_lineas = []
        cuartas_lineas = []

        for i in lista:
            operacion = i.split(' ')
            primer_operando = operacion[0]
            segundo_operando = operacion[2]
            operador = operacion[1]

            cantidad_digitos_primer_operando = len(primer_operando)
            cantidad_digitos_segundo_operando = len(segundo_operando)

            if operador == '+' or operador == '-':
                if primer_operando.isnumeric() and segundo_operando.isnumeric():
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
                        
                        if operador == '+':
                            operacion = int(primer_operando) + int(segundo_operando)
                        elif operador == '-':
                            operacion = int(primer_operando) - int(segundo_operando)

                        largo_suma = len(str(operacion))
                        espacios_cuarta_linea = largo_operador_mas_largo - largo_suma

                        cuarta_linea = ''
                        for i in range(espacios_cuarta_linea):
                            cuarta_linea += ' '
                        
                        cuarta_linea += str(operacion)

                        primeras_lineas.append(primera_linea)
                        segundas_lineas.append(segunda_linea)
                        terceras_lineas.append(tercera_linea)
                        cuartas_lineas.append(cuarta_linea)
  
                    else:
                        return 'Error: Numbers cannot be more than four digits.'

                else:
                    return 'Error: Numbers must only contain digits.'

            else:
                return "Error: Operator must be '+' or '-'."


        primera_linea_global = '    '.join(primeras_lineas)
        segunda_linea_global = '    '.join(segundas_lineas)
        tercera_linea_global = '    '.join(terceras_lineas)
        cuarta_linea_global = '    '.join(cuartas_lineas)

        if resultados:
            formateo = f'{primera_linea_global}\n{segunda_linea_global}\n{tercera_linea_global}\n{cuarta_linea_global}'
        else:
            formateo = f'{primera_linea_global}\n{segunda_linea_global}\n{tercera_linea_global}'
        
        return formateo

    else:
        return 'Error: Too many problems.'