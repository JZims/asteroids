import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


    

def main():
    pygame.init()
   
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # PyGame Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    #Containers
    Player.containers = (updateable, drawable)
    Asteroid.containerables = (updateable, drawable, asteroids)
    AsteroidField.containers = updateable
    # Game Objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill((0, 0, 0))
        player.draw(screen)
        # Limit's frame rate to 60fps
        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
