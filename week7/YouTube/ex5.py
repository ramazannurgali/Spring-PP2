import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

hero = pygame.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect()

sc.fill(WHITE)
sc.blit(hero, (100, 50))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    sc.fill(WHITE)
    sc.blit(hero, (100, 50))
    pygame.display.update()