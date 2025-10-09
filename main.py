import pygame
pygame.init()
#initialise screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PolygonCreator")

points = [] # to store the points of the polygon
selected_point = None # to store the selected point for dragging
dragging = False # to indicate if we are dragging a point
polygon_closed = False # to indicate if the polygon is closed


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
            for i, point in enumerate(points):
                dx = pos[0] - point[0]
                dy = pos[1] - point[1]
                if dx**2 + dy**2 < 100: #within 10 pixels
                    selected_point = i
                    dragging = True
                    break
            else:
                points.append(pos)
        
        if event.type == pygame.MOUSEMOTION and dragging and selected_point is not None:
            if pygame.mouse.get_pressed()[0]: # left button is held down
                pos = pygame.mouse.get_pos()
                points[selected_point] = pos
            else:
                dragging = False
                selected_point = None
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False
            selected_point = None
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            polygon_closed = not polygon_closed
            
        # deleting point s
        if event.type == pygame.KEYDOWN and selected_point is not None:
            if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                points.pop(selected_point)
                selected_point = None
                dragging = False
            
        if event.type == pygame.KEYDOWN:
            print("Key pressed:", event.key)

    
    # loop through the points list and for each draw small circle sgreen radius 5
    for i, point in enumerate(points):
        colour = (255, 255, 0) if i == selected_point else (0, 255, 0)
        pygame.draw.circle(screen, colour, point, 5)
        
        
    
    if len(points) > 1:
        if polygon_closed and len(points) > 2:
            pygame.draw.polygon(screen, (255, 0, 0), points, 2)
        else:
            pygame.draw.lines(screen, (0, 0, 255), False, points, 2 )
        


            

    pygame.display.flip()





