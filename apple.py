from random import randint
import config 

def generate_pos():
    return [randint(1, config.screen_x_size), randint(1, config.screen_y_size)]

class Apple:
    counter = 0
    def __init__(self):
        self.position = generate_pos()
    
    def eaten_apple(self):
        self.counter += 1 
        self.position = generate_pos()