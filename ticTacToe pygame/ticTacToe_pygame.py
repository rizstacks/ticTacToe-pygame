import pygame

pygame.init()
screenSize = 900
screen = pygame.display.set_mode((screenSize, screenSize))
clock = pygame.time.Clock()
running = True
squareSize = 600
boardState = []
print("test")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    screen.fill("black")

    pygame.draw.rect(screen, "white", pygame.Rect((screenSize - squareSize)/2,(screenSize - squareSize)/2,squareSize,squareSize))
    pygame.draw.rect(screen, "black", pygame.Rect((screenSize - squareSize)/2 + 5,(screenSize - squareSize)/2 + 5,squareSize - 10,squareSize - 10))
    pygame.draw.line(screen, "red", (200, 350), (700, 350), 7)
    pygame.draw.line(screen, "red", (200, 550), (700, 550), 7)
    pygame.draw.line(screen, "red", (550, 700), (550, 200), 7)
    pygame.draw.line(screen, "red", (350, 700), (350, 200), 7)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
