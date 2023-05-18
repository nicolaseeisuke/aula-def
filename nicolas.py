import trigonometria, os
os.system ('cls')

catO = float(input('Qual o cateto oposto?'))
catA = float(input('Qual o cateto adjacente?'))

print(f'seno = {trigonometria.seno(catO,catA)}')
print(f'cosseno = {trigonometria.cosseno(catO,catA)}')
print(f'tangente = {trigonometria.tag(catO,catA)}')