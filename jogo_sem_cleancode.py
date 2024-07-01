import os

# ler arquivo txt
def ler_ranking():
    if not os.path.exists("ranking.txt"):
        return []
    with open("ranking.txt", "r") as file:
        ranking = []
        for line in file:
            nome, pontos = line.strip().split(":")
            ranking.append((nome, int(pontos)))
    return sorted(ranking, key=lambda x: x[1], reverse=True)

# salvar ranking
def salvar_ranking(ranking):
    with open("ranking.txt", "w") as file:
        for nome, pontos in ranking:
            file.write(f"{nome}:{pontos}\n")

# atualizar o ranking
def atualizar_ranking(nome, pontos):
    ranking = ler_ranking()
    ranking.append((nome, pontos))
    ranking = sorted(ranking, key=lambda x: x[1], reverse=True)[:10]  # top 10
    salvar_ranking(ranking)

# bonequinho da forca
def mostrar_forca(erros):
    estagios = [
        """
         -----
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]
    print(estagios[erros])

# nome do jogador
nome_jogador = input("Qual é o seu nome? ")

# escolher palavra do jogo
palavra = "python"

letras_usuario = []

chances = 6
erros = 0

ganhou = False

while True:
    # mostrar bonequinho da forca
    mostrar_forca(erros)

    # logica
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"\nVocê tem {chances - erros} chances")

    tentativa = input("Escolha uma letra para adivinhar: ")

    if tentativa.lower() in letras_usuario:
        print("Você já tentou essa letra.")
        continue

    letras_usuario.append(tentativa.lower())

    if tentativa.lower() not in palavra.lower():
        erros += 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if erros == chances or ganhou:
        break

# calculo de pontos: chances restantes x os pts
pontos = (chances - erros) * 10

if ganhou:
    print(f"Parabéns, você ganhou. A palavra era: {palavra}")
else:
    mostrar_forca(erros)  # Mostrar a forca completa ao perder
    print(f"Você perdeu! A palavra era: {palavra}")

print(f"{nome_jogador}, você fez {pontos} pontos.")

# atualizar o ranking
atualizar_ranking(nome_jogador, pontos)

# mostrar ranking atualizado
print("\nRanking top 10 dos melhores pontuadores:")
ranking = ler_ranking()
for i, (nome, pontos) in enumerate(ranking, start=1):
    print(f"{i}. {nome} - {pontos} pontos")
