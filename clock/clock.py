import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((829, 836))
clock = pygame.time.Clock()


dial = pygame.image.load(r'/Users/ernrsahar/Desktop/PP2_projects/lab7/clock/clock.png')
l = pygame.image.load(r'/Users/ernrsahar/Desktop/PP2_projects/lab7/clock/leftarm.png')
r = pygame.image.load(r'/Users/ernrsahar/Desktop/PP2_projects/lab7/clock/rightarm.png')

rect = dial.get_rect(center=(415, 418))

while True:
    screen.fill((255, 255, 255))  
    screen.blit(dial, rect.topleft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    t = datetime.now().time()
    
   
    a1 = - (t.second * 6)  
    n = pygame.transform.rotate(l, a1)
    rect2 = n.get_rect(center=rect.center)
    screen.blit(n, rect2.topleft)

   
    a2 = - (t.minute * 6)  
    n2 = pygame.transform.rotate(r, a2)
    rect3 = n2.get_rect(center=rect.center)
    screen.blit(n2, rect3.topleft)

    pygame.display.flip()
    clock.tick(60)
