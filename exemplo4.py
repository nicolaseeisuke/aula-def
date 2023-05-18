def area(base, altura):
    return base*altura/2

base =  float(input('Digite a base do triângulo em cm:'))
altura =  float(input('Digite a altura do triângulo em cm:'))

print(f'A área do retângulo é {area(base,altura)} cm²')
print(f'A área do retângulo é {area(100,20)} cm²')
print(f'A área do retângulo é {area(10,8)} cm²')
print(f'A área do retângulo é {area(54,39)} cm²')
