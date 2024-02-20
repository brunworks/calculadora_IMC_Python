def calcular_IMC(peso, altura):
    return peso / (altura ** 2)

peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite a sua altura em metros: '))


imc = calcular_IMC(peso, altura)
print(f'Seu IMC é: {imc:.2f}')