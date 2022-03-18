pregunta = ('Agrega un numero para saber si es par o impar \r\n')
pregunta += ' (Escribe "cerrar" para salir de la app) \r\n' 
preguntar = True

while preguntar: #While se ejecuta mientras una variable sea verdadera
    numero = input(pregunta)

    if numero == 'cerrar':
        preguntar = False
    else:
        numero = int(numero)

        if numero % 2 == 0:
            print(f'{numero} es un numero par!')
        else:
            print(f'{numero} es un numero impar!')