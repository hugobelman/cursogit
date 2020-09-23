a = input('Ingresa el lado del cuadrado: ')

try:
    a = float(a)
    print(f'Con el lado {a} el area del cuadrado es {a*a}')
except:
    print('Usted no puede hacer semejante barbaridad')
