import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Constantes do jogo
LARGURA, ALTURA = 800, 600
COR_FUNDO = (0, 0, 0)
COR_JOGADOR = (255, 255, 255)
COR_BOLA = (255, 255, 255)
VELOCIDADE_JOGADOR = 7
VELOCIDADE_BOLA_X = 5
VELOCIDADE_BOLA_Y = 5
TAMANHO_JOGADOR_LARGURA = 15
TAMANHO_JOGADOR_ALTURA = 100
TAMANHO_BOLA = 15

# Criação da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong - Para Iniciantes em Python")
relogio = pygame.time.Clock()

# Funções do jogo
def desenhar_jogador(x, y):
    """Desenha um jogador (raquete) na tela"""
    pygame.draw.rect(tela, COR_JOGADOR, (x, y, TAMANHO_JOGADOR_LARGURA, TAMANHO_JOGADOR_ALTURA))

def desenhar_bola(x, y):
    """Desenha a bola na tela"""
    pygame.draw.rect(tela, COR_BOLA, (x, y, TAMANHO_BOLA, TAMANHO_BOLA))

def desenhar_placar(placar_esquerda, placar_direita):
    """Desenha o placar na tela"""
    fonte = pygame.font.Font(None, 74)
    texto_esquerda = fonte.render(str(placar_esquerda), True, COR_JOGADOR)
    texto_direita = fonte.render(str(placar_direita), True, COR_JOGADOR)
    tela.blit(texto_esquerda, (LARGURA // 4, 20))
    tela.blit(texto_direita, (3 * LARGURA // 4, 20))

def desenhar_linha_central():
    """Desenha a linha central pontilhada"""
    for y in range(0, ALTURA, 20):
        if y % 40 == 0:
            pygame.draw.rect(tela, COR_JOGADOR, (LARGURA // 2 - 2, y, 4, 20))

def mover_jogador(teclas, jogador_y, jogador_lado):
    """Move o jogador baseado nas teclas pressionadas"""
    if jogador_lado == "esquerda":
        if teclas[pygame.K_w] and jogador_y > 0:
            jogador_y -= VELOCIDADE_JOGADOR
        if teclas[pygame.K_s] and jogador_y < ALTURA - TAMANHO_JOGADOR_ALTURA:
            jogador_y += VELOCIDADE_JOGADOR
    else:  # direita
        if teclas[pygame.K_UP] and jogador_y > 0:
            jogador_y -= VELOCIDADE_JOGADOR
        if teclas[pygame.K_DOWN] and jogador_y < ALTURA - TAMANHO_JOGADOR_ALTURA:
            jogador_y += VELOCIDADE_JOGADOR
    return jogador_y

def mover_bola(bola_x, bola_y, velocidade_x, velocidade_y):
    """Move a bola e verifica colisões com as paredes"""
    bola_x += velocidade_x
    bola_y += velocidade_y
    
    # Colisão com as paredes superior e inferior
    if bola_y <= 0 or bola_y >= ALTURA - TAMANHO_BOLA:
        velocidade_y = -velocidade_y
    
    return bola_x, bola_y, velocidade_x, velocidade_y

def verificar_colisao_raquete(bola_x, bola_y, jogador_esquerda_y, jogador_direita_y):
    """Verifica colisão da bola com as raquetes"""
    # Colisão com jogador esquerdo
    if (bola_x <= TAMANHO_JOGADOR_LARGURA and 
        jogador_esquerda_y <= bola_y <= jogador_esquerda_y + TAMANHO_JOGADOR_ALTURA):
        return "esquerda"
    
    # Colisão com jogador direito
    if (bola_x >= LARGURA - TAMANHO_JOGADOR_LARGURA - TAMANHO_BOLA and 
        jogador_direita_y <= bola_y <= jogador_direita_y + TAMANHO_JOGADOR_ALTURA):
        return "direita"
    
    return None

def reiniciar_bola():
    """Reinicia a bola no centro com direção aleatória"""
    bola_x = LARGURA // 2 - TAMANHO_BOLA // 2
    bola_y = ALTURA // 2 - TAMANHO_BOLA // 2
    velocidade_x = VELOCIDADE_BOLA_X * random.choice([-1, 1])
    velocidade_y = VELOCIDADE_BOLA_Y * random.choice([-1, 1])
    return bola_x, bola_y, velocidade_x, velocidade_y

def mostrar_tela_inicio():
    """Mostra a tela de início do jogo"""
    tela.fill(COR_FUNDO)
    fonte_titulo = pygame.font.Font(None, 74)
    fonte_instrucoes = pygame.font.Font(None, 36)
    
    titulo = fonte_titulo.render("PONG", True, COR_JOGADOR)
    instrucao1 = fonte_instrucoes.render("Jogador Esquerdo: W (cima) e S (baixo)", True, COR_JOGADOR)
    instrucao2 = fonte_instrucoes.render("Jogador Direito: SETA ↑ (cima) e SETA ↓ (baixo)", True, COR_JOGADOR)
    instrucao3 = fonte_instrucoes.render("Pressione ESPAÇO para começar", True, COR_JOGADOR)
    
    tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, ALTURA // 4))
    tela.blit(instrucao1, (LARGURA // 2 - instrucao1.get_width() // 2, ALTURA // 2))
    tela.blit(instrucao2, (LARGURA // 2 - instrucao2.get_width() // 2, ALTURA // 2 + 40))
    tela.blit(instrucao3, (LARGURA // 2 - instrucao3.get_width() // 2, ALTURA // 2 + 100))
    
    pygame.display.flip()
    
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def mostrar_vencedor(vencedor):
    """Mostra tela de vitória"""
    tela.fill(COR_FUNDO)
    fonte = pygame.font.Font(None, 74)
    fonte_instrucoes = pygame.font.Font(None, 36)
    
    if vencedor == "esquerda":
        texto = fonte.render("Jogador Esquerdo Venceu!", True, COR_JOGADOR)
    else:
        texto = fonte.render("Jogador Direito Venceu!", True, COR_JOGADOR)
    
    instrucao = fonte_instrucoes.render("Pressione ESPAÇO para jogar novamente ou ESC para sair", True, COR_JOGADOR)
    
    tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 3))
    tela.blit(instrucao, (LARGURA // 2 - instrucao.get_width() // 2, ALTURA // 2))
    
    pygame.display.flip()
    
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Função principal do jogo
def jogo_pong():
    # Posições iniciais
    jogador_esquerda_y = ALTURA // 2 - TAMANHO_JOGADOR_ALTURA // 2
    jogador_direita_y = ALTURA // 2 - TAMANHO_JOGADOR_ALTURA // 2
    bola_x, bola_y, velocidade_bola_x, velocidade_bola_y = reiniciar_bola()
    
    # Placar
    placar_esquerda = 0
    placar_direita = 0
    placar_maximo = 5
    
    # Estado do jogo
    jogo_ativo = True
    
    # Loop principal do jogo
    while jogo_ativo:
        # Processamento de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    jogo_ativo = False
        
        # Movimento dos jogadores
        teclas = pygame.key.get_pressed()
        jogador_esquerda_y = mover_jogador(teclas, jogador_esquerda_y, "esquerda")
        jogador_direita_y = mover_jogador(teclas, jogador_direita_y, "direita")
        
        # Movimento da bola
        bola_x, bola_y, velocidade_bola_x, velocidade_bola_y = mover_bola(
            bola_x, bola_y, velocidade_bola_x, velocidade_bola_y
        )
        
        # Verificar colisões com as raquetes
        colisao = verificar_colisao_raquete(bola_x, bola_y, jogador_esquerda_y, jogador_direita_y)
        if colisao:
            velocidade_bola_x = -velocidade_bola_x
            # Aumenta um pouco a velocidade a cada rebatida
            velocidade_bola_x *= 1.1
            velocidade_bola_y *= 1.1
        
        # Verificar se a bola saiu da tela (ponto)
        if bola_x < 0:
            placar_direita += 1
            bola_x, bola_y, velocidade_bola_x, velocidade_bola_y = reiniciar_bola()
        elif bola_x > LARGURA:
            placar_esquerda += 1
            bola_x, bola_y, velocidade_bola_x, velocidade_bola_y = reiniciar_bola()
        
        # Verificar se alguém ganhou
        if placar_esquerda >= placar_maximo or placar_direita >= placar_maximo:
            vencedor = "esquerda" if placar_esquerda >= placar_maximo else "direita"
            mostrar_vencedor(vencedor)
            # Reiniciar o jogo
            placar_esquerda = 0
            placar_direita = 0
            bola_x, bola_y, velocidade_bola_x, velocidade_bola_y = reiniciar_bola()
        
        # Desenhar tudo
        tela.fill(COR_FUNDO)
        desenhar_linha_central()
        desenhar_jogador(0, jogador_esquerda_y)
        desenhar_jogador(LARGURA - TAMANHO_JOGADOR_LARGURA, jogador_direita_y)
        desenhar_bola(bola_x, bola_y)
        desenhar_placar(placar_esquerda, placar_direita)
        
        # Atualizar a tela
        pygame.display.flip()
        relogio.tick(60)  # 60 FPS

# Executar o jogo
if __name__ == "__main__":
    mostrar_tela_inicio()
    jogo_pong()