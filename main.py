import pygame
import random

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo da Cobra Piranha e Covarde")

cobra_piranha = [(100,50)]
direcao = (10,0)
comida = (300, 200)

def desenhar():
    tela.fill((0, 0, 0))
    for parte in cobra_piranha:
        pygame.draw.rect(tela, (0, 255, 0), (*parte, 10, 10))

    pygame.draw.rect(tela, (255, 0, 0), (*comida, 10, 10))
    pygame.display.update()

rodando = True
relogio = pygame.time.Clock()
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                direcao = (0, -10)
            elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                direcao = (0, 10)
            elif evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                direcao = (-10, 0)
            elif evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                direcao = (10, 0)

    nova_cabeca = (cobra_piranha[0][0] + direcao[0], cobra_piranha[0][1] + direcao[1])
    cobra_piranha.insert(0, nova_cabeca)
    cobra_piranha.pop()

    desenhar()
    relogio.tick(15)

pygame.quit()