import pygame, random, sys
pygame.init()

tela = pygame.display.set_mode((400, 300))
x, y = 200, 150
vel_x, vel_y = 20, 0
cobra = [[x, y]]
comida = [random.randrange(0, 400, 20), random.randrange(0, 300, 20)]
clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and vel_y == 0: vel_x, vel_y = 0, -20
            if e.key == pygame.K_DOWN and vel_y == 0: vel_x, vel_y = 0, 20
            if e.key == pygame.K_LEFT and vel_x == 0: vel_x, vel_y = -20, 0
            if e.key == pygame.K_RIGHT and vel_x == 0: vel_x, vel_y = 20, 0

    x += vel_x; y += vel_y
    cobra.append([x, y])
    if [x, y] == comida:
        comida = [random.randrange(0, 400, 20), random.randrange(0, 300, 20)]
    else:
        del cobra[0]

    if x < 0 or y < 0 or x >= 400 or y >= 300 or [x, y] in cobra[:-1]:
        pygame.quit(); sys.exit()

    tela.fill((0, 0, 0))
    for parte in cobra: pygame.draw.rect(tela, (0, 255, 0), (*parte, 20, 20))
    pygame.draw.rect(tela, (255, 0, 0), (*comida, 20, 20))
    pygame.display.update()
    clock.tick(10)
