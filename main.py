import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot



        

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for obj in updatable:
            obj.update(dt)

    
        for asteriod in asteroids:
            if player.collision(asteriod) == True:
                print("Game over!")
                return 
            
            for shot in shots:
                if asteriod.collision(shot) == True:
                    asteriod.split()  
                    shot.kill()
                   
        
        pygame.display.flip()

        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

