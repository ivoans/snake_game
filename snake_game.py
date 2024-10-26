import pygame
from random import randint

pygame.init()

#--Constants--#

#--FUNCTIONS--#
def game():
    WIDTH, HEIGHT = 600, 400
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    SNAKE_SPEED = 10
    BLOCK_SIZE = 20
    DIRECTION = 'RIGHT'
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    #--POSITIONS--#
    snake_pos = [[100, 50]]
    direccion = [BLOCK_SIZE, 0]
    food_pos = [randint(1, (WIDTH//BLOCK_SIZE)) * BLOCK_SIZE, randint(1, (HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]    

    #--CLOCK--#
    clock = pygame.time.Clock()
    
    puntaje = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and DIRECTION != 'DOWN':
                    direccion = [0, -BLOCK_SIZE]
                    DIRECTION = 'UP'
                elif event.key == pygame.K_DOWN and DIRECTION != 'UP':
                    direccion = [0, BLOCK_SIZE]
                    DIRECTION = 'DOWN'
                elif event.key == pygame.K_LEFT and DIRECTION != 'RIGHT':
                    direccion = [-BLOCK_SIZE, 0]
                    DIRECTION = 'LEFT'
                elif event.key == pygame.K_RIGHT and DIRECTION != 'LEFT':
                    direccion = [BLOCK_SIZE, 0]
                    DIRECTION = 'RIGHT'
        
        # Move the snake
        if direccion != [0, 0]:  # Solo mover si hay dirección
            new_pos = [snake_pos[0][0] + direccion[0], snake_pos[0][1] + direccion[1]]
            snake_pos.insert(0, new_pos)

            # Eat the food
            if snake_pos[0] == food_pos:
                food_pos = [randint(1, (WIDTH//BLOCK_SIZE)) * BLOCK_SIZE, randint(1, (HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]
                puntaje += 1
            else:
                snake_pos.pop()

            # Collision with the walls
            if (snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT or snake_pos[0] in snake_pos[1:]):
                run = False

            # Draw the screen
            SCREEN.fill(BLACK)
            for pos in snake_pos:
                pygame.draw.rect(SCREEN, GREEN, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(SCREEN, RED, (food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.display.update()
            clock.tick(SNAKE_SPEED)

    print('Puntaje:', puntaje)
    pygame.quit()

game()