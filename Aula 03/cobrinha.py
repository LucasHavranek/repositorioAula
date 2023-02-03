import turtle
import random
import time

screen = turtle.Screen()
screen.title('Jogo da cobrinha')

score = 0
tempo = 20
length_snake = 0

screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('white')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('yellow')
food.penup()
food.goto(100, 100)

def right():
    snake.direction = 'right'

def left():
    snake.direction = 'left'

def up():
    snake.direction = 'up'

def down():
    snake.direction = 'down'

def center():
    snake.goto(0,0)

screen.listen()
screen.onkeypress(right, 'Right')
screen.onkeypress(left, 'Left')
screen.onkeypress(up, 'Up')
screen.onkeypress(down, 'Down')


while tempo > 0:
    screen.update()
    if snake.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        length_snake += 1
        score += 10
        tempo += 2.5
        screen.title(f'Score: {score}')
    time.sleep(0.1)
    tempo -= 0.1
    screen.title(f'Time: {tempo} - Score: {score}')
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)

screen.title(f'Game over. Score: {score}')
snake.goto(0,0)
snake.direction = 'stop'
screen.mainloop()
