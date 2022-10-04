# criar jogo da cobrinha com python
# colocar o jogo no streamlit
# sem o pygame
import random

import streamlit as st


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.body = [[x, y]]
        self.direction = "right"
        self.score = 0

    def move(self):
        if self.direction == "right":
            self.x += 1
        elif self.direction == "left":
            self.x -= 1
        elif self.direction == "up":
            self.y -= 1
        elif self.direction == "down":
            self.y += 1

        self.body.insert(0, [self.x, self.y])
        self.body.pop()

    def grow(self):
        self.body.insert(0, [self.x, self.y])
        self.score += 1

    def check_collision(self):
        if self.x > 19 or self.x < 0 or self.y > 19 or self.y < 0:
            return True

        for block in self.body[1:]:
            if self.x == block[0] and self.y == block[1]:
                return True

        return False


class Food:
    def __init__(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)

    def new_location(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)


def main():
    st.title("Snake Game")
    st.write("Use the arrow keys to move the snake")
    st.write("Press space to start the game")

    snake = Snake(10, 10)
    food = Food()

    game_over = False

    while not game_over:
        if st.button("Start"):
            game_over = False
            snake = Snake(10, 10)
            food = Food()

        while not game_over:
            # check for collision
            if snake.check_collision():
                game_over = True
                break

            # check if snake has eaten food
            if snake.x == food.x and snake.y == food.y:
                snake.grow()
                food.new_location()

            # move snake
            snake.move()

            # create game board
            game_board = [["blank" for _ in range(20)] for _ in range(20)]

            # add snake to game board
            for x, y in snake.body:
                game_board[y][x] = "snake"

            # add food to game board
            game_board[food.y][food.x] = "food"

            # display game board
            st.write(f"Score: {snake.score}")
            for row in game_board:
                for block in row:
                    if block == "blank":
                        st.write("⬛", end="")
                    elif block == "snake":
                        st.write("🟩", end="")
                    elif block == "food":
                        st.write("🟥", end="")
                st.write("")

            # control snake
            if st.button("Up"):
                snake.direction = "up"
            elif st.button("Down"):
                snake.direction = "down"
            elif st.button("Left"):
                snake.direction = "left"
            elif st.button("Right"):
                snake.direction = "right"
                
if __name__ == "__main__":
    main()
