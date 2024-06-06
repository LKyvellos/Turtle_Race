import turtle
import random

scn= turtle.Screen()
turtle.title("TURTLE_RACE")
t_one=turtle.Turtle()
t_one.penup()
t_one.goto(-300,200)
t_one.shape("turtle")
t_one.fillcolor("green")
t_two=t_one.clone()
t_two.fillcolor("blue")
t_two.penup()
t_two.goto(-300,-200)
t_two.shape("turtle")


t_one.fd(500)
t_one.pendown()
t_one.circle(40)
t_one.penup()
t_one.lt(90)
t_one.fd(40)
t_one.rt(90)
t_one.bk(500)


t_two.fd(500)
t_two.pendown()
t_two.circle(40)
t_two.penup()
t_two.lt(90)
t_two.fd(40)
t_two.rt(90)
t_two.bk(500)

dice = [1,2,3,4,5,6]

while t_one.pos() < (220,200) and t_two.pos() < (220,-200):
    diceOutcome = random.choice(dice)
    print("result of dice roll: ",diceOutcome)
    print("Number of steps")
    print(20*diceOutcome)
    t_one.fd(20*diceOutcome)
    diceOutcome2 = random.choice(dice)
    print("result of dice roll 2: ",diceOutcome2)
    print("Number of steps 2")
    print(20*diceOutcome2)
    t_two.fd(20*diceOutcome2)

    if t_one.pos() >= (200,200):
        print("GREEEN TURTOLL WINNSSSS")
        break
    elif t_two.pos() >= (200,-200):
        print("BLOOOO TURTOLL WINNNSSS")
        break

turtle.done()


