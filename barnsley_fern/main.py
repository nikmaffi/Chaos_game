import pygame
from Barnsley import Barnsley

WINDOW_SIZE = (1200, 900)
FPS = 60

SCALE_X = (-6, 6)
SCALE_Y = (-1, 11)

def main():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)
    done = False

    b = Barnsley(SCALE_X, SCALE_Y, WINDOW_SIZE)

    pygame.display.set_caption("Barnsley fern")

    while not done:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        b.update()

        screen.fill((0, 0, 0))

        b.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":    
    main()