# criar jogo da cobrinha com python
# colocar o jogo no streamlit
import random

import streamlit as st
import pygame

st.title('Jogo da Cobrinha')

st.write("Clique no botão para iniciar o jogo")

if st.button('Iniciar'):
    st.write('Jogo iniciado')

    pygame.init()
    pygame.display.set_caption('Snake Game')
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 40)


    def draw_text(text, color, x, y):
        img = font.render(text, True, color)
        screen.blit(img, (x, y))


    def draw_grid():
        for x in range(0, 600, 20):
            pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
        for y in range(0, 600, 20):
            pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))


    def draw_snake(screen, color, snake_list, snake_size):
        for x, y in snake_list:
            pygame.draw.rect(screen, color, [x, y, snake_size, snake_size])


    def message(msg, color):
        mesg = font.render(msg, True, color)
        screen.blit(mesg, [100, 250])


    def game_loop():
        game_over = False
        game_close = False
        x1 = 300
        y1 = 300
        x1_change = 0
        y1_change = 0
        snake_list = []
        Length_of_snake = 1
        snake_size = 20
        foodx = round(random.randrange(0, 600 - snake_size) / 20.0) * 20.0
        foody = round(random.randrange(0, 600 - snake_size) / 20.0) * 20.0
        while not game_over:
            while game_close:
                screen.fill((0, 0, 0))
                draw_text("You Lost! Press Q-Quit or C-Play Again", (255, 255, 255), 50, 250)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            game_loop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_size
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_size
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_size
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_size
                        x1_change = 0
            if x1 >= 600 or x1 < 0 or y1 >= 600 or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            screen.fill((0, 0, 0))
            draw_grid()
            pygame.draw.rect(screen, (255, 0, 0), [foodx, foody, snake_size, snake_size])
            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > Length_of_snake:
                del snake_list[0]
            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True
            draw_snake(screen, (0, 255, 0), snake_list, snake_size)
            pygame.display.update()
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, 600 - snake_size) / 20.0) * 20.0
                foody = round(random.randrange(0, 600 - snake_size) / 20.0) * 20.0
                Length_of_snake += 1
            clock.tick(15)
        pygame.quit()
        quit()


    game_loop()
else:
    st.write('Jogo não iniciado')
