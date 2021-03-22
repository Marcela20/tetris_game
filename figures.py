from constans import *

start_x = round(dis_width / 2)
start_y = 0
fig_0 = [[start_x, start_y]]
fig_1 = [[start_x, start_y], [start_x - element_size, start_y], [start_x, start_y - element_size],
         [start_x + element_size, start_y - element_size]]
fig_2 = [[start_x, start_y], [start_x + element_size, start_y], [start_x, start_y - element_size],
         [start_x - element_size, start_y - element_size]]
fig_3 = [[start_x, start_y], [start_x - element_size, start_y], [start_x - element_size, start_y - element_size],
         [start_x, start_y - element_size]]
fig_4 = [[start_x, start_y], [start_x + element_size, start_y], [start_x - element_size, start_y],
         [start_x - 2 * element_size, start_y]]
fig_5 = [[start_x, start_y], [start_x + element_size, start_y], [start_x - element_size, start_y],
         [start_x - element_size, start_y - element_size]]
fig_6 = [[start_x, start_y], [start_x + element_size, start_y], [start_x - element_size, start_y],
         [start_x + element_size, start_y - element_size]]
fig_7 = [[start_x, start_y], [start_x + element_size, start_y], [start_x - element_size, start_y],
         [start_x, start_y - element_size]]

list_of_figures = [fig_1, fig_2, fig_3, fig_4, fig_5, fig_6, fig_7]
# list_of_figures = [fig_4]