

quantidade_atividadesA = int(input("Informe os dias para a Atividade A: "))

quantidade_atividadesB = int(input("Informe os dias para a Atividade B: "))

quantidade_atividadesC = int(input("Informe os dias para a Atividade C: "))


if quantidade_atividadesA and quantidade_atividadesB and quantidade_atividadesC < 0:
    print("Os dias nao podem ser negativos")
else:
    total_dias = quantidade_atividadesA + quantidade_atividadesB + quantidade_atividadesC
    print(f"Total de dias: {total_dias}")