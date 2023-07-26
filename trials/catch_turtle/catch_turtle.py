import random
import turtle
import time
import threading

def main():
    game_screen = turtle.Screen()
    game_screen.bgcolor("light slate gray")
    game_screen.screensize(400, 400)

    spawn_rate = int(turtle.numinput("Tortoise ", "Select the spawn rate[1-10]:\n[0.5] fast\n[1] normal\n[1.5] slow"))
    global time_left
    time_left = int(turtle.numinput("Tortoise ", "(The timer starts after you press OK.)\n\n Counts down from :  "))

    if not 1 <= spawn_rate <= 10:
        spawn_rate = 1

    main_turtle = turtle.Turtle()
    main_turtle.shape("turtle")
    main_turtle.penup()
    main_turtle.hideturtle()

    colors0 = ["black","black","white"]
    colors = ["red","purple","blue","light blue","dark green","yellow","deep pink","indigo","dark magenta","dark cyan"]
    sizes = [0.7, 1, 1.5, 2]
    global score
    score = 0
    score_turtle = turtle.Turtle()
    score_turtle.penup()
    score_turtle.hideturtle()

    title_turtle = turtle.Turtle()
    title_turtle.penup()
    title_turtle.hideturtle()
    title_turtle.goto(-195,370)
    title_turtle.write("The Tortoise Trainer", font=("Courier",25,"italic","bold"))

    time_turtle = turtle.Turtle()
    time_turtle.penup()
    time_turtle.hideturtle()
    time_turtle.goto(-460,280)

    score_turtle.goto(-460,320)
    score_turtle.write(f"Score : {score}", font=("Courier",20,"normal"))

    def click_turtle(x, y):
        global score
        main_turtle.hideturtle()
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score : {score}", font=("Courier",20,"normal"))

    def turtle_generate():
        random_color = random.choice(colors)
        random_color2 = random.choice(colors0)
        main_turtle.color(random_color2, random_color)
        random_size = random.choice(sizes)
        main_turtle.turtlesize(random_size)
        x = random.randint(-370, 330)
        y = random.randint(-370, 330)
        main_turtle.goto(x, y)
        main_turtle.showturtle()

    def timer_loop():
        global time_left
        for _ in range(time_left):
            time.sleep(1)
            time_turtle.clear()
            time_left -= 1
            time_turtle.write(f"Time Left : {time_left}", font=('Courier', 20, 'normal'))
        time_turtle.clear()
        time_turtle.goto(0, 50)
        time_turtle.write(f"Time Is Over!", align="center", font=('Courier', 23, 'normal'))
        time.sleep(2)
        turtle.Screen().bye()
    def turtle_generator():
        for _ in range(88):
            main_turtle.onclick(click_turtle)
            turtle_generate()
            time.sleep(0.7)
            main_turtle.hideturtle()

    thread_timer = threading.Thread(target=timer_loop)
    thread_generator = threading.Thread(target=turtle_generator)

    thread_timer.start()
    thread_generator.start()
    turtle.mainloop()

while True:
    main()
    time.sleep(1)
    rq = turtle.textinput("Tortoise", " 'r' to restart\n'q' to quit  : ")
    if rq.lower() == "q":
        turtle.bye()
        break