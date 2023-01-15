# Programa 7.2 Jogo da Forca

número = int(input("digite um número de 0 à 6 para selecionar uma Palavra Secreta: "))
palavras = ["bola", "papagaio", "futebol", "carro", "onibus", "CPU", "igreja"]
palavra = palavras[(número * 776) % len(palavras)]
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0

while True:
    escolhido = palavra  
    senha = ''
    for letra in escolhido:
       
        senha += letra if letra in acertos else '.'
    print (senha)
    if senha == escolhido:
        print ("Você acertou!")
        break
    tentativa = input ("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print ("Você ja tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in escolhido:
            acertos += tentativa
        else:
            erros += 1
            print ("Você errou!!")
    print("X====:++\nX      :    ")
    print("X       O   " if erros >= 1 else "X")
    linha2 = []
    if erros == 2:
        linha2.append("    |   ")
    elif erros == 3:
        linha2.append ("  \|  ")
    elif erros >= 4:
        linha2.append ("   |/  ")
    print(f"X{linha2}")
    linha3 = []
    if erros == 5:
        linha3.append ("  /   ")
    elif erros >= 6:
        linha3.append ("   / \  ")
    print(f"X{linha3}")
    print("X\n========")
    if erros == 6:
        print("Enforcado!!!")
        print(f"A Palavra secreta era: {escolhido}")
        break
            
