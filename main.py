import pygame

print('Inicio da aplicação')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Fim da aplicação')

print('Inicio do loop')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit()  # Close window
            quit()  # end pygame
