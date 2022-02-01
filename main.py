import pygame
from snake import Snake
from fruit import Fruit
from random import randint

class Game:
    def __init__(self):
        # Init pygame, create the window using the determined size
        # change the name of the window
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Cobrinha')
        self.clock = pygame.time.Clock()

        # Variable to stop the game
        self.playing = True

        self.x = randint(72, 800-32)
        self.y = randint(0, 600-32)
        self.snake = Snake(self.x, self.y)

        self.rand_coord()
        self.fruit = Fruit(self.x, self.y, 32)
        

    
    def run(self):
        while self.playing:
            self.clock.tick(60)
            self.update()
            self.draw()
            self.events()

        pygame.quit()

    def update(self):

        
        if self.snake.snake[0].x >= 800 - 32 or self.snake.snake[0].x <= 0:
            self.game_over()

        if self.snake.snake[0].y >= 600 - 32 or self.snake.snake[0].y <= 0:
            self.game_over()
        
        for i in range(2, len(self.snake.snake)):
            if pygame.Rect.colliderect(self.snake.snake[0], self.snake.snake[i]):
                self.game_over()

        if pygame.Rect.colliderect(self.snake.snake[0], self.fruit.rect):
            del self.fruit
            self.rand_coord()
            self.fruit = Fruit(self.x, self.y,32)
            self.snake.add_part()

        
        self.snake.move()

    def game_over(self):
        del self.snake
        self.rand_coord('snake')
        self.snake = Snake(self.x, self.y)

        del self.fruit
        self.rand_coord()
        self.fruit = Fruit(self.x, self.y,32)

    def rand_coord(self, obj='none'):
        if obj == 'snake':
            self.x = randint(72, 800-32)
            self.y = randint(0, 600-32)
        else:
            self.x = randint(0, 800-32)
            self.y = randint(0, 600-32)

    def draw(self):
        self.screen.fill('black')

        self.fruit.draw(self.screen)
        self.snake.draw(self.screen)

        pygame.display.update()

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.playing = False
            
            self.snake.snake_events(event)

