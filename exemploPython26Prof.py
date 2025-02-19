import random

# def adivinhe_o_numero():
print("Bem-vindo ao jogo 'Adivinhe o Número'!")
print("O objetivo é adivinhar um número entre 1 e 100.")
print("Digite 'sair' a qualquer momento para encerrar o jogo.")
    
# Gerar o número secreto
numero_secreto = random.randint(1, 100)
tentativas = 0  # Contador de tentativas
    
while True:
        tentativa = input("Digite seu palpite: ")
        
        # Verificar se o jogador quer sair
        if tentativa.lower() == "sair":
            print("Você decidiu encerrar o jogo. Até a próxima!")
            break
        
        # Verificar se a entrada é válida
        if not tentativa.isdigit():
            print("Por favor, insira um número válido!")
            continue
        
        tentativa = int(tentativa)  # Converter para inteiro
        tentativas += 1  # Incrementar contador
        
        # Verificar o palpite
        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break
        elif tentativa < numero_secreto:
            print("Mais alto!")
        else:
            print("Mais baixo!")

# Executar o jogo
# adivinhe_o_numero()