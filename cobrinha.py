import pygame
import random
import sys

pygame.init()

LARGURA = 600
ALTURA = 400
TAMANHO_QUADRADO = 20
VELOCIDADE = 10

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

def desenhar_cobra(tamanho_quadrado, pixels):
    for pixel  in pixels:
        pygame.draw.rect(tela, VERDE, (pixel[0], pixel[1], tamanho_quadrado, tamanho_quadrado))

def mostrar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("arial", 25)
    texto = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
    tela.blit(texto, [10, 10])

def rodar_jogo():
    fim_jogo = False
    x = LARGURA // 2
    y = ALTURA // 2
    velocidade_x = 0
    velocidade_y = 0
    
    corpo_cobra = []
    comprimento_cobra = 1
    
    comida_x = round(random.randrange(0, LARGURA - TAMANHO_QUADRADO) / 20.0) * 20.0
    comida_y = round(random.randrange(0, ALTURA - TAMANHO_QUADRADO) / 20.0) * 20.0
    
    relogio = pygame.time.Clock()
    pontuacao = 0
    
    while not fim_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Movimentação
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and velocidade_x == 0:
                    velocidade_x = -TAMANHO_QUADRADO
                    velocidade_y = 0
                elif evento.key == pygame.K_RIGHT and velocidade_x == 0:
                    velocidade_x = TAMANHO_QUADRADO
                    velocidade_y = 0
                elif evento.key == pygame.K_UP and velocidade_y == 0:
                    velocidade_y = -TAMANHO_QUADRADO
                    velocidade_x = 0
                elif evento.key == pygame.K_DOWN and velocidade_y == 0:
                    velocidade_y = TAMANHO_QUADRADO
                    velocidade_x = 0                    
            # Atualiza a posição da cobra
            x += velocidade_x
            y += velocidade_y
            
            # Verifica a colisão com as bordas
            if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
                fim_jogo = True

            tela.fill(PRETO)
            pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_QUADRADO, TAMANHO_QUADRADO])
            
            # Atualiza o corpo da cobra
            corpo_cobra.append([x,y])
            if len(corpo_cobra) > comprimento_cobra:
                del corpo_cobra[0]
            
            # Verifica a colisão com o próprio corpo
            for parte in corpo_cobra[:-1]:
                if parte == [x,y]:
                    fim_jogo = True
            
            desenhar_cobra(TAMANHO_QUADRADO, corpo_cobra)
            mostrar_pontuacao(pontuacao)
            
            pygame.display.update()
            
            # Quando a cobra come a comida
            if x == comida_x and y == comida_y:
                comida_x = round(random.randrange(0, LARGURA - TAMANHO_QUADRADO) / 20.0) * 20.0
                comida_y = round(random.randrange(0, ALTURA - TAMANHO_QUADRADO) / 20.0) * 20.0
                comprimento_cobra += 1
                pontuacao += 10
                
            relogio.tick(VELOCIDADE)
            
    # Tela de fim de jogo
    tela.fill(PRETO)
    fonte = pygame.font.SysFont("arial", 35)
    texto = fonte.render(f"Fim de jogo! Pontuação: {pontuacao}", True, VERMELHO)
    tela.blit(texto, [LARGURA / 6, ALTURA / 3])
    pygame.display.update()
    pygame.time.delay(2500)
            
# Executa o jogo
while True:
    rodar_jogo()
            
            
            