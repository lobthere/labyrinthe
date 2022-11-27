import pygame
import random as r

"""explaining""""""
0 = wall
1 = no wall
2 = start
3 = end
4 = extorior wall
"""""""""

"""init"""
INIT_SQUARE = 20
INIT_RANGE_LABYRIHTHE = 41 #ne choisir que des nombres impaires et superieur a 12

"""the Table"""
X_SIDE = list(range(INIT_SQUARE, (INIT_RANGE_LABYRIHTHE + 2) * INIT_SQUARE, INIT_SQUARE))
Y_SIDE = list(range(INIT_SQUARE, (INIT_RANGE_LABYRIHTHE + 2) * INIT_SQUARE, INIT_SQUARE))


"""Init everything"""
pygame.init()

"""The Display"""
DISPLAY_X = (INIT_SQUARE * INIT_RANGE_LABYRIHTHE ) + INIT_RANGE_LABYRIHTHE * 2
DISPLAY_Y = (INIT_SQUARE * INIT_RANGE_LABYRIHTHE ) + INIT_RANGE_LABYRIHTHE * 2
color = (255, 255, 255)
surface = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))
pygame.display.set_caption("Labyrinthe")
surface.fill(color)
pygame.display.flip()

"""The board"""
POSITION = [0, 0, 0, 0]
SAVE = list(range(0, INIT_RANGE_LABYRIHTHE * INIT_SQUARE + INIT_RANGE_LABYRIHTHE * INIT_SQUARE * 1000, 1))
COLOR = 'red'

"""if running"""
running = True

"""draw the rectangles"""
x = 0
y = 0
count = 0
count_2 = 0
count_3 = 0
random = 2
random_2 = 2
while random % 2 != 1:
    random = r.randint(0, INIT_RANGE_LABYRIHTHE - 1)
while random_2 % 2 != 1:
    random_2 = r.randint(0, INIT_RANGE_LABYRIHTHE - 1)

for i in range(0, INIT_RANGE_LABYRIHTHE, 1):
    if x % 2 == 0:
        for z in range(0, INIT_RANGE_LABYRIHTHE, 1):
            POSITION[0] = X_SIDE[x]
            POSITION[1] = Y_SIDE[y]


            if POSITION[0] == INIT_SQUARE:
                if z != 0:
                    if z == random:
                        POSITION[2] = 2
                    else:
                        POSITION[2] = 4
                else:
                    POSITION[2] = 4
            elif POSITION[0] == INIT_SQUARE * INIT_RANGE_LABYRIHTHE:
                if count_3 == random_2:
                    POSITION[2] = 3
                else:
                    POSITION[2] = 4
            elif POSITION[1] == INIT_SQUARE:
                POSITION[2] = 4
            elif POSITION[1] == INIT_SQUARE * INIT_RANGE_LABYRIHTHE:
                POSITION[2] = 4
            else :
                POSITION[2] = 0
            

            if POSITION[2] == 0 or POSITION[2] == 4:
                COLOR = 'black'
            elif POSITION[2] == 2:
                COLOR = 'green'
            elif POSITION[2] == 3:
                COLOR = 'red'
            
            pygame.draw.rect(surface, COLOR, [POSITION[0], POSITION[1], INIT_SQUARE, INIT_SQUARE])
            SAVE[count] = [POSITION[0], POSITION[1], POSITION[2], POSITION[3]]
            y+=1
            count += 1
            count_3 +=1
            pygame.display.update()
    if x % 2 == 1:
        for z in range(0, INIT_RANGE_LABYRIHTHE, 1):
            POSITION[0] = X_SIDE[x]
            POSITION[1] = Y_SIDE[y]

            if POSITION[1] == INIT_SQUARE:
                POSITION[2] = 4
            elif POSITION[1] == INIT_SQUARE * INIT_RANGE_LABYRIHTHE:
                POSITION[2] = 4
            elif count_2 % 2 == 0:
                POSITION[2] = 0
            elif count_2 % 2 == 1:
                POSITION[2] = 1
                POSITION[3] = r.randint(1, 9)

            if POSITION[2] == 0:
                COLOR = 'black'
            elif POSITION[2] == 1:
                COLOR = 'white'
            elif POSITION[2] == 4:
                COLOR = 'black'
            
            if POSITION[2] == 1:
                POSITION[3] = r.randint(0, 9)
            pygame.draw.rect(surface, COLOR, [POSITION[0], POSITION[1], INIT_SQUARE, INIT_SQUARE])
            count_2 += 1
            SAVE[count] = [POSITION[0], POSITION[1], POSITION[2], POSITION[3]]
            y += 1
            count += 1
            pygame.display.update()
        count_2 = 0
    x += 1
    y = 0
    count_3 = 0
    count_2 = 0

pygame.display.update()

count_4 = 0
save_i = list(range(0, INIT_RANGE_LABYRIHTHE * INIT_SQUARE + INIT_RANGE_LABYRIHTHE * INIT_SQUARE * 1000, 1))

for i in range(0, INIT_RANGE_LABYRIHTHE * INIT_RANGE_LABYRIHTHE):
    if SAVE[i][2] == 1:
        save_i[count_4] = [i]
        count_4 += 1


random_2 = r.randint(0, count_4)
temp = SAVE[count_4]


print('fin')


"""keep the game awake"""
while running:

    """check if there is an event"""
    for event in pygame.event.get():

        """if event equal exit : we stop the boucle"""
        if event.type == pygame.QUIT:
            running = False

pygame.display.update()