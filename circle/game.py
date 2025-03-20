import pygame

pygame.init()
W, H = 600, 400
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Red ball")
clock = pygame.time.Clock()
FPS = 60

x, y = W // 2, H // 2
speed = 5
radius = 25
flLeft = flRight = False
flUp = flDown = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
            if event.key == pygame.K_UP:
                flUp = True
            elif event.key == pygame.K_DOWN:
                flDown = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                flLeft = flRight = False
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                flUp = flDown = False

   
    a, b = pygame.display.get_window_size()

   
    if flLeft and x - speed >= radius:
        x -= speed
    elif flRight and x + speed <= a - radius:
        x += speed

   
    if flUp and y - speed >= radius:
        y -= speed
    elif flDown and y + speed <= b - radius:
        y += speed

  
    sc.fill((255, 255, 255))

   
    pygame.draw.circle(sc, (255, 0, 0), (x, y), radius)

   
    pygame.display.update()
    clock.tick(FPS)