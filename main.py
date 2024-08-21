import pygame
import sys
from constants     import *
from player        import Player
from asteroid      import Asteroid
from asteroidfield import AsteroidField
from shot          import Shot

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots     = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidf = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for thing in updatable:
            thing.update(dt)
        
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()

        dt = game_clock.tick(60) / 1000

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides(asteroid):
                    shot.kill()
                    asteroid.split()

        


if __name__ == "__main__":
    main()
