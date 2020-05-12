import pygame

pygame.init()

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption(" :-) ")
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (800, 600))

window.blit(bg, (0, 0))

# PLAYERS VAR
x1 = 200
y1 = 300
x2 = 400
y2 = 400
color = (255,255,255)

pygame.draw.circle(window, (255, 0, 0), (x1, y1), 15)
pygame.draw.circle(window, color, (x2, y2), 20)

pygame.display.update()
run = True
while run:
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if dist < 1225: # (r1+r2)**2
        color = (255,0,0)
    else:
        color = (255,255,255)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x1 += 1

    if keys[pygame.K_LEFT]:
        x1 -= 1

    if keys[pygame.K_UP]:
        y1 -= 1

    if keys[pygame.K_DOWN]:
        y1 += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(bg, (0, 0))
    pygame.draw.circle(window, (255, 0, 0), (x1, y1), 15)
    pygame.draw.circle(window, color, (400, 400), 20)
    pygame.display.update()

pygame.quit()