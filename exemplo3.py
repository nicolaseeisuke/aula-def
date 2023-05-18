import os
os.system ('cls')

def calcularImc(peso, altura):
    return peso/altura**2

peso = float(input('Digite seu peso: '))
altura = float(input("Digite sua altura:  "))

resultado = calcularImc(peso, altura)
print(f'Seu IMC é {resultado:.2f} kg/m²')
