import pygame

print('Setup start')
pygame.init()

window = pygame.display.set_mode(size=(600, 480))
print('Setup end')

print('Loop')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # fecha janela
            quit()
