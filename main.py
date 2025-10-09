import pygame
pygame.init()
#initialise screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PolygonCreator")

running = True
# main loop work swhen the window is open
while running:
    screen.fill((30, 30, 30))
    # event loop for quitting the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()





