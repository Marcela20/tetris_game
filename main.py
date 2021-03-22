import sys
import random
import pygame
from figures import *
import collections
from Figure import *
from pygame.locals import *

def draw_figures_down(figures):
    for element in figures:
        pygame.draw.rect(window, element.color, element.create_element())


def giveMeNewFigure(figures):
    color = 'PURPLE'
    color_of_figure.clear()
    figure_in_use = random.choice(figures)
    if figure_in_use == fig_1:
        color = "YELLOW"
    if figure_in_use == fig_2:
        color = "CYAN"
    if figure_in_use == fig_3:
        color = "MAGENTA"
    if figure_in_use == fig_4:
        color = "BLUE"
    if figure_in_use == fig_5:
        color = "GREEN"
    if figure_in_use == fig_6:
        color = "RED"
    color_of_figure.append(color)

    index_of_fig = list_of_figures.index(figure_in_use)
    list_of_indexes.clear()
    list_of_indexes.append(index_of_fig)
    return Figure(figure_in_use, color_of_figure[0])


def row_dissapear(it, count):
    list_s = []
    list_of_y_of_s_down = []
    list_of_s_above = []
    if it % 7 == 0:
        for square in list_of_squares_down:
            list_of_y_of_s_down.append(int(square.coord_y))
        c_y = [int(y) for y, count in collections.Counter(list_of_y_of_s_down).items() if
               count >= (dis_width / element_size)]
        if len(c_y) >= 1:
            for num in c_y:
                count += 1

        for square in list_of_squares_down:
            if int(square.coord_y) in c_y:
                list_s.append(square)

        for square in list_of_squares_down:
            for y in c_y:
                if int(square.coord_y) < y:
                    list_of_s_above.append(square)

        for s in list_s:
            if s in list_of_squares_down:
                list_of_squares_down.remove(s)

        for sq in list_of_s_above:
            sq.move_down()
    return count


def message(msg, color, coords, size):
    font = pygame.font.Font('freesansbold.ttf', size)
    mesg = font.render(msg, True, color)
    window.blit(mesg, coords)


def button(text):
    font_obj = pygame.font.Font('freesansbold.ttf', 32)
    text_surface_obj = font_obj.render(text, True, WHITE, RED)
    text_rect_obj = text_surface_obj.get_rect()
    button = window.blit(text_surface_obj, text_rect_obj)
    return button


def score_count(number, color):
    font = pygame.font.Font('freesansbold.ttf', 30)
    mesg = font.render(number, True, color)
    window.blit(mesg, [dis_width - 20, 0])


def game_lost(squares):
    for square in squares:
        if square.coord_y == 0:
            return True

pygame.init()

ready_to_spin = True
fpsClock = pygame.time.Clock()

figure_in_use = giveMeNewFigure(list_of_figures)
moving_right = True
moving_left = True


while True:
    window.fill((0, 0, 0))
    fpsClock.tick(FPS)

    # wychodzenie z gry
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    colide = False

    # fragment odpowiadajcy za poruszanie sie w dol i na boki
    figure_in_use.move_down(move_down_speed_iterator)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            direction = 'RIGHT'
        if event.key == pygame.K_LEFT:
            direction = 'LEFT'
        if event.key == pygame.K_DOWN:
            if figure_in_use.collide(list_of_squares_down) == False:
                direction = "DOWN"
        figure_in_use.move_sideways(direction, list_of_squares_down)
    direction = ''

    # fragment odpowiadajacy za samo obracanie sie figury :)
    if event.type == pygame.KEYDOWN and ready_to_spin:
        if event.key == pygame.K_UP:
            figure_in_use.spin()
            ready_to_spin = False
    elif event.type == pygame.KEYUP:
        ready_to_spin = True

    # sprawdz czy fig. dotknela ziemi lub innej figury
    if figure_in_use.collide(list_of_squares_down):
        list_of_squares_down += figure_in_use.squares
        figure_in_use = giveMeNewFigure(list_of_figures)
    counter = row_dissapear(move_down_speed_iterator, counter)
    row_dissapear(move_down_speed_iterator, counter)
    move_down_speed_iterator += 0.5
    figure_in_use.draw()
    draw_figures_down(list_of_squares_down)

    figure_in_use.return_to_window()
    message(f"scores: {counter}", RED, [dis_width - 100, 0], 15)

    if game_lost(list_of_squares_down):
        message("game over", RED, [(dis_width / 2) - 70, (dis_height / 2) - 30], 30)
        move_down_speed_iterator = 1
        buttonik = button("play again!")
        direction = "STOP"
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if buttonik.collidepoint(mouse_pos):
                list_of_squares_down.clear()
                counter = 0

    pygame.display.update()

