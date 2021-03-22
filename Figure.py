import math
from Square import *


class Figure:
    def __init__(self, coordinates_of_squares, color):
        self.squares = []
        self.color = color
        for element in coordinates_of_squares:
            self.squares.append(Square(element[0], element[1], self.color))

    def spin(self):

        x2 = self.squares[0].coord_x
        y2 = self.squares[0].coord_y
        for square in self.squares:
            x3 = (square.coord_x - x2) * 0 + (square.coord_y - y2) * 1 + x2
            y3 = math.fabs((square.coord_x - x2) * 1 + (square.coord_y - y2) * 0 - y2)
            square.coord_x = x3
            square.coord_y = y3

    def return_to_window(self):
        for square in self.squares:
            if square.coord_x >= dis_width:
                dir = "LEFT"
                for sq in self.squares:
                    sq.move_sideways(dir)
            elif square.coord_x < 0:
                dir = "RIGHT"
            elif square.coord_y < 0:
                dir = "DOWN"
                for sq in self.squares:
                    sq.move_sideways(dir)

    def move_down(self, iterator):
        if iterator % 5 == 0:
            for square in self.squares:
                if square.coord_y<=dis_height-element_size:
                    square.move_down()

    def move_sideways(self, dir, sq_down):
        # sprawdz czy moge sie ruszyc w bok
        for square in self.squares:
            for sq in sq_down:
                if square.coord_x == sq.coord_x + element_size and square.coord_y == sq.coord_y and dir == 'LEFT':
                    return
                if square.coord_x == sq.coord_x - element_size and square.coord_y == sq.coord_y and dir == "RIGHT":
                    return

            if dir == 'LEFT' and square.coord_x == 0:
                return

            if dir == 'RIGHT' and square.coord_x == dis_width - element_size:
                return

        # jezeli tak to przesuwam wszystkie kwadratys

        for square in self.squares:
            square.move_sideways(dir)

    def draw(self):
        for square in self.squares:
            pygame.draw.rect(window, square.color, square.create_element())

    def collide(self, sq_down):
        for square in self.squares:
            if square.coord_y >= dis_height - element_size:
                return True
            for sq in sq_down:
                if square.coord_y + element_size == sq.coord_y and square.coord_x == sq.coord_x:
                    return True
        return False
