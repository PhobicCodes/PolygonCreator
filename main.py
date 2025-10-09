import pygame
pygame.init()
#initialise screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PolygonCreator")

points = [] # to store the points of the polygon
running = True
# main loop work swhen the window is open
while running:
    screen.fill((30, 30, 30))
    # event loop for quitting the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            points.append(pos)
    
    # loop through the points list and for each draw small circle sgreen radius 5
    for point in points:
        pygame.draw.circle(screen, (0, 255, 0), point, 5)
    # if there are more than 1 point draw lines between them
    if len(points) > 1:
        pygame.draw.lines(screen, (0, 0, 255), False, points, 2)  
    
    # if thre are more than 2 points function that connects points in order (not closed shape yet)
    if len(points) > 2:
        pygame.draw.polygon(screen, (255, 0, 0), points, 2)  
        
            

    pygame.display.flip()





