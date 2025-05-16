#Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"IMC: {imc:.2f} - Abaixo do peso")
elif 18.5 <= imc < 25:
    print(f"IMC: {imc:.2f} - Peso normal")
else:
    print(f"IMC: {imc:.2f} - Acima do peso")

