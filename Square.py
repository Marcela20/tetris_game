from constans import *


class Square:
    def __init__(self, coord_x, coord_y, color=BLUE, width = element_size, hight = element_size):
        self.width = width
        self.hight = hight
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.color = color

    def create_element(self):
        element = pygame.Rect(self.coord_x, self.coord_y, self.width, self.hight)
        return element

    def move_down(self):
        if self.coord_y <= dis_height-element_size:
            self.coord_y += self.hight

    def move_sideways(self, direction_of_movement):
        if direction_of_movement == "RIGHT":
            self.coord_x += element_size
        if direction_of_movement == "LEFT":
            self.coord_x -= element_size
        if direction_of_movement == "DOWN":
            self.coord_y += element_size
        if direction_of_movement == "STOP":
            self.coord_x += 0
    def draw(self, color):
        pygame.draw.rect(window, color, self.create_element())

