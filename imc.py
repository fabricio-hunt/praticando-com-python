peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"IMC: {imc:.2f} - Abaixo do peso")
elif 18.5 <= imc < 25:
    print(f"IMC: {imc:.2f} - Peso normal")
else:
    print(f"IMC: {imc:.2f} - Acima do peso")

