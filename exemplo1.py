def exibir(num, msg):
    print(f'A mensagem é {msg}')
    print(f'O número é num: {num} ')

msg = input('Digite sua mensagem: ')
num = int(input('Digite um número: '))

exibir(num, msg)