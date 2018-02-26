from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 255 ]

matrix = new_matrix()
print_matrix(matrix)
ident(matrix)
print_matrix(matrix)

a = [[12,10,17],[19,13,12],[13,14,15]]
b = [[13,14],[15,16],[17,18]]
print_matrix(matrix_mult(a, b))


matriY = new_matrix()
add_edge(matriY, 150, 150, 0, 150, 300, 0)
add_edge(matriY, 150, 300, 0, 175, 350, 0)
add_edge(matriY, 175, 350, 0, 250, 240, 0)


add_edge(matriY, 350, 150, 0, 350, 300, 0)
add_edge(matriY, 275, 350, 0, 350, 300, 0)
add_edge(matriY, 250, 240, 0, 275, 350, 0)


add_edge(matriY, 250, 150, 0, 250, 240, 0)



draw_lines(matriY,screen,color)




display(screen)
