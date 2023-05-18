import os

soma = lambda a,b: a+b
subt = lambda a,b: a-b
mult = lambda a,b: a*b
div = lambda a,b: a/b

menu = ['Soma', 'subtração','Multiplicação','divisão','Sair']

while True:
    os.system('cls')
    print('Calculadora lambda')
    for n, item in enumerate(menu):
        print(f'[{n+1}] - {item}')
    op = int(input('Digite uma opção: '))
    if op == 5: break
    elif str(op) not in '1234': print('opção invalida')
    else:
        n1 = float(input('Digite o 1° número: '))
        n2 = float(input('Digite o 2° número: '))
        if op == 1: print(f'{n1} + {n2} = {soma(n1, n2):.0f}')
        elif op == 2: print(f'{n1} - {n2} = {subt(n1, n2):.0f}')
        elif op == 3: print(f'{n1} * {n2} = {mult(n1, n2):.0f}')
        else: print(f'{n1} / {n2} = {div(n1, n2):.0f}')
    input('\nEnter continua...')

os.system('cls')
print('Obriagado por ultilizar nosso sismtema\n Volte sempre')
