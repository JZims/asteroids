import pygame
import sys
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


    

def main():
    pygame.init()
   
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # PyGame Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
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

            updatable.update(dt)

            # check for collisions
            for asteroid in asteroids:
                if player.collision(asteroid):
                    print("Game Over!")
                    sys.exit()

            for shot in shots:
                for asteroid in asteroids:
                    if shot.collision(asteroid):
                        shot.kill()
                        asteroid.split()
                        

            screen.fill("black")

            for obj in drawable:
                obj.draw(screen)

            pygame.display.flip()

            # limit the framerate to 60 FPS
            dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
