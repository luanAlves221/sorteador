import random
import pygame
import time
pygame.init()

sorteado = pygame.mixer.Sound("sorteado.wav")

print("bem-vindo")

pessoas = [""]
pessoas = input("Escreva o nome das pessoas que participarão do sorteio").split(',')

itens = [""]
itens = input("Insira os itens para sortear").split(',')

quantidade = int(input("quanto de cada ítem?"))

pessoa_s = random.choice(pessoas)
itens_s = random.choice(itens)

print(f"O sorteado foi: {pessoa_s} e ganhou {quantidade} {itens_s}")
sorteado.play()
time.sleep(3)
