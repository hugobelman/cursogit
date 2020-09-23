a = input('Ingresa el lado del cuadrado: ')

if (type(a) == type(str)):
    print('Usted no puede hacer semejante barbaridad')
else:
    a = int(a)
    print(f'Area del cuadrado es {a*a}')