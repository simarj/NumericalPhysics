import pygame,pymunk,sys
pygame.init()
screen=pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
    screen.fill((217,217,217))
    
