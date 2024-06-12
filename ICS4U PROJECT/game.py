import sys

import pygame
from scripts.entities import PhysicsEntity
from scripts.utils import load_image


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('I wanna be the Guy Clone')
        self.screen = pygame.display.set_mode((640, 480))

        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'decor': load_image('Pygame_Assets/Tiles/decor.png'),
            'player': load_image('Pygame_Assets/Tiles/grey_square.png'),
        }

        print(self.assets)
        self.player = PhysicsEntity(self, 'player', (1, 1), (1, 1))

    def run(self):
        while True:
            self.display.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False


            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()