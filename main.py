import pygame
from snake import Snake

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Cobrinha')
        self.clock = pygame.time.Clock()

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