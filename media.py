
nota1 = float  (input("Digite a nota 1: "))
nota2 = float  (input("Digite a nota 2: "))
nota3 = float  (input("Digite a nota 3: "))

#calcular média
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f'Aluno provado com a média:{media: .1f}')
elif media <= 5 or media <7:
    print(f'Aluno em recuperação com a média: {media: .1f}')
elif media < 5:
    print(f'Aluno reprovado com a média: {media: .1f}')


