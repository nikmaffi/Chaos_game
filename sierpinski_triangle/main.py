import pygame
from Sierpinski import Sierpinski

WINDOW_SIZE = (1000, 900)
FPS = 60

VERTEX = [(500, 50), (50, 850), (930, 800)]
STARTING_POINT = (500, 450)

def main():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)
    done = False

    s = Sierpinski(VERTEX, STARTING_POINT)

    pygame.display.set_caption("Sierpinski triangle")

    while not done:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        s.update()

        screen.fill((0, 0, 0))

        s.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    while True:
        if input() == "ok":
            break
    
    main()