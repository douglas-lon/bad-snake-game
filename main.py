import pygame
from snake import Snake

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

        self.x = 100
        self.y = 100
        self.snake = Snake(self.x, self.y)
        

    
    def run(self):
        while self.playing:
            self.clock.tick(60)
            self.update()
            self.draw()
            self.events()

        pygame.quit()

    def update(self):
        
        self.snake.move()
        
        for i in range(2, len(self.snake.snake)):
            if pygame.Rect.colliderect(self.snake.snake[0], self.snake.snake[i]):
                self.game_over()

    def game_over(self):
        del self.snake
        self.snake = Snake(self.x, self.y)

    def draw(self):
        self.screen.fill('black')

        self.snake.draw(self.screen)

        pygame.display.update()

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.playing = False
            
            self.snake.snake_events(event)

                


if __name__ == '__main__':
    g = Game()
    g.run()