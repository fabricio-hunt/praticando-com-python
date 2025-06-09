distancia = float(input("Digite a distância (em km): "))

if distancia <= 100:
    print('O valor do pedágio é R$10,00')
elif distancia > 100 and distancia <= 200:
    print('O valor do pedágio é R$20,00')
elif distancia > 200:
    print('O valor do pedágio é R$30,00')