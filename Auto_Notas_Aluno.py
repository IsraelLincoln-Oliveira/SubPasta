alunos = []

def calcular_media(notas):
    resultado = sum(notas) / len(notas)
    return resultado #Função para calcular a média das notas

for aluno in range(30):                
    alunos.append(input("Digite o nome do aluno: ")) #Adiciona o nome do aluno à lista

    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i + 1}: ").replace(",", "."))
        notas.append(nota) #Adiciona a nota à lista de notas

    resultado = calcular_media(notas)

    if resultado >= 7:
        print("Aprovado") #Imprime "Aprovado" se a média for maior ou igual a 7
    elif resultado >= 5:
        print("Recuperação") #Imprime "Recuperação" se a média for maior ou igual a 5 e menor que 7
    else:
        print("Reprovado") #Imprime "Reprovado" se a média for menor que 5






    