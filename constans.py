import pygame

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
PURPLE = (102, 0, 102)

dis_width = 280
dis_height = 380
window_size = (dis_width, dis_height)
window = pygame.display.set_mode(window_size, 0, 32)
pygame.display.set_caption("tetris")
element_size = 20
counter = 0
color_of_figure = []
FPS = 20
direction = ""
move_down_speed_iterator = 0

list_of_indexes = []
list_of_squares_down = []
