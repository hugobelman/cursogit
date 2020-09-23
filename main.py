a = input('Ingresa el lado del cuadrado: ')

try:
    a = float(a)
    print(f'Area del cuadrado es {a*a}')
except:
    print('Usted no puede hacer semejante barbaridad')