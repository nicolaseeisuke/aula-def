def soma(a, b):
    return a + b


while True:
    n1 = int(input('Qual o 1° número? '))
    n2 = int(input('Qual o 2° número? '))

    print(soma(n1, n2))
    if (input('Deseja continuar')) in 'nN':
        break
