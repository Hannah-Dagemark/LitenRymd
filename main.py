import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()

running = True 

def update():
    print("Update tick")

def render():
    screen.fill("cyan")
    pygame.display.flip()
    print("Graphic tick")

def save_game():
    print("Saving game")

while running:

    update()
    render()

    clock.tick(60)  # limits FPS to 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            save_game()

pygame.quit()
