# MELHORIAS APLICADAS
# Lucas Lopes Lettnin (manhã): Dividiu as funções para deixar o código mais responsável, sem problemas futuros pois cada função terá responsabilidades unicas.
# Luis Felipe Quineper (noite): Utilizou o list comprehensions e funções auxiliares para evitar repetições. Assim tornando o código menor e funcional.
# Pedro Martins Vergara (manhã): Realizou uma melhor organização do código com indentação e espaçamento consistentes. 
# Em grupo também decidimos deixar as variáveis e funções com nomes mais claros e significativos.

import os

def ler_ranking(filename="ranking.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        ranking = [line.strip().split(":") for line in file]
    return sorted(((nome, int(pontos)) for nome, pontos in ranking), key=lambda x: x[1], reverse=True)

def salvar_ranking(ranking, filename="ranking.txt"):
    with open(filename, "w") as file:
        lines = [f"{nome}:{pontos}\n" for nome, pontos in ranking]
        file.writelines(lines)


def atualizar_ranking(nome, pontos, filename="ranking.txt"):
    ranking = ler_ranking(filename)
    ranking.append((nome, pontos))
    ranking = sorted(ranking, key=lambda x: x[1], reverse=True)[:10]
    salvar_ranking(ranking, filename)

def mostrar_forca(erros):
    estagios = [
        "  -----\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "  -----\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  -----\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  -----\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  -----\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "  -----\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "  -----\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
    ]
    print(estagios[erros])

def obter_palavra():
    return "python"

def exibir_status(palavra, letras_usuario, chances, erros):
    mostrar_forca(erros)
    print(" ".join(letra if letra in letras_usuario else "_" for letra in palavra))
    print(f"\nVocê tem {chances - erros} chances")

def verificar_tentativa(tentativa, letras_usuario):
    if tentativa in letras_usuario:
        print("Você já tentou essa letra.")
        return False
    return True

def calcular_pontos(chances, erros):
    return (chances - erros) * 10

def jogar_forca():
    nome_jogador = input("Qual é o seu nome? ")
    palavra = obter_palavra()
    letras_usuario = []
    chances = 6
    erros = 0
    ganhou = False

    while erros < chances and not ganhou:
        exibir_status(palavra, letras_usuario, chances, erros)
        tentativa = input("Escolha uma letra para adivinhar: ").lower()
        if not verificar_tentativa(tentativa, letras_usuario):
            continue
        letras_usuario.append(tentativa)
        if tentativa not in palavra:
            erros += 1
        ganhou = all(letra in letras_usuario for letra in palavra)

    pontos = calcular_pontos(chances, erros)
    print(f"\nParabéns, você ganhou. A palavra era: {palavra}" if ganhou else f"\nVocê perdeu! A palavra era: {palavra}")
    print(f"{nome_jogador}, você fez {pontos} pontos.")
    atualizar_ranking(nome_jogador, pontos)

def exibir_ranking():
    print("\nRanking top 10 dos melhores pontuadores:")
    for i, (nome, pontos) in enumerate(ler_ranking(), start=1):
        print(f"{i}. {nome} - {pontos} pontos")

def main():
    jogar_forca()
    exibir_ranking()

if __name__ == "__main__":
    main()

# MELHORIAS APLICADAS
# Lucas Lopes Lettnin (manhã): Dividiu as funções para deixar o código mais responsável, sem problemas futuros pois cada função terá responsabilidades unicas.
# Luis Felipe Quineper (noite): Utilizou o list comprehensions e funções auxiliares para evitar repetições. Assim tornando o código menor e funcional.
# Pedro Martins Vergara (manhã): Realizou uma melhor organização do código com indentação e espaçamento consistentes. 
# Em grupo também decidimos deixar as variáveis e funções com nomes mais claros e significativos.