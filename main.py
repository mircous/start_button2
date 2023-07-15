import pygame

pygame.init()

screen = pygame.display.set_mode((620, 800))

back = pygame.image.load("start_screen.png")
button =  pygame.image.load("button.png")


back2 = pygame.image.load("red.png")

button_width = 200
button_height = 100
zomaze = pygame.transform.scale(button,(button_width, button_height))
zomaze_back_surati = pygame.transform.scale(back2, (620, 800))
charcho = zomaze.get_rect()
charcho2 = zomaze.get_rect()
charcho.center = (200, 400)
charcho2.center = (450, 400)


runnig = True
tamashshii = False
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if (charcho.collidepoint(mouse_pos) or charcho2.collidepoint(mouse_pos))  and  tamashshii == False:
                print("Start button clicked!!!")
                tamashshii = True
            elif (charcho.collidepoint(mouse_pos) or charcho2.collidepoint(mouse_pos)) and tamashshii == True:
                print("Start button clicked!!!")
                tamashshii = False
        if tamashshii:
            screen.blit(zomaze_back_surati, (0, 0))   
            screen.blit(zomaze, charcho)
            screen.blit(zomaze, charcho2)

            pygame.display.flip()
        
        else:
            screen.blit(back, (-300, 0))   
            screen.blit(zomaze, charcho)
            screen.blit(zomaze, charcho2)

            pygame.display.flip()