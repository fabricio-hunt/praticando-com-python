idade = int(input("Digite sua idade: "))
tem_documento = input("Tem documento?(sim/não): ")

if idade >= 18 and tem_documento == "sim":
    print(f"Sua idade é {idade} anos e tem documento, Pode dirigir")
else:
    print("Sua idade é {idade} e não pode dirigir")             