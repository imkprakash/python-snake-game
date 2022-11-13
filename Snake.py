import turtle
import random
import time
delay = 0.1
score = 0
high_score = 0

# Screen
wn = turtle.Screen()
wn.title("Snake game by KSHITIZ")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)


# Snake head
head = turtle.Turtle()
head.speed(0)  # animation screen
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)  # animation screen
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.shape("square")
pen.color("white")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0    High Score: 0", align="center",
          font=("Courier", 24, "normal"))

is_paused = False
# Functions


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def toggle_pause():
    global is_paused
    if is_paused:
        is_paused = False
    else:
        is_paused = True


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_down, "s")
wn.onkeypress(toggle_pause, "p")

# Main game loop
while True:
    if not is_paused:
        wn.update()
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(
            score, high_score), align="center", font=("Courier", 24, "normal"))

        # Check for collision with border
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide the segment
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # reset delay
            delay = 0.1

            # Reset score
            score = 0
            pen.clear()
            pen.write("Score: {}    High Score: {}".format(
                score, high_score), align="center", font=("Courier", 24, "normal"))

        # checking for collision with the food
        if head.distance(food) < 20:
            # move food to a random spot
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            food.goto(x, y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            # Reducing delay
            delay -= 0.001

            # increase score

            score += 1
            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}    High Score: {}".format(
                score, high_score), align="center", font=("Courier", 24, "normal"))

        # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # move segment 0 to head
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        # Check for body collisions
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"

                for segment in segments:
                    segment.goto(1000, 1000)

                segments.clear()

                # Reset delay
                delay = 0.1

                score = 0
                pen.clear()
                pen.write("Score: {}    High Score: {}".format(
                    score, high_score), align="center", font=("Courier", 24, "normal"))

    else:
        wn.update()
        pen.clear()
        pen.write("Game Paused!", align="center",
                  font=("Courier", 24, "normal"))

    time.sleep(delay)


wn.mainloop()
