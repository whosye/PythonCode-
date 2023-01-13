
from tkinter import Y
import turtle 
from random import randrange as rg 
import winsound

wn = turtle.Screen()
wn.title('TENIS')
wn.bgcolor('RED')
wn.setup(width=800, height = 600)
wn.tracer(0)

# A 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color('brown')
paddle_a.penup() # nekreslit cary 
paddle_a.goto(-350,0)

# B 
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color('black')
paddle_b.penup() # nekreslit cary 
paddle_b.goto(350,0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('pink')
ball.penup() # nekreslit cary 
ball.goto(0,0)
# inkrementace pohybu o 2 pixely ve svou smerech 
ball.dx = 0.2
ball.dy = 0.2 

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('PlayerA = 0  PlayerB = 0', align='center', font=(('Courier',24,'normal')))

#Score
score_a=0
score_b=0




def paddle_a_up():
    y = paddle_a.ycor() #return Y coordinate
    y += 20 
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor() #return Y coordinate
    y -= 20 
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #return Y coordinate
    y += 20 
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor() #return Y coordinate
    y -= 20 
    paddle_b.sety(y)



# keyboard bindgin 
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')


while True:
    wn.update()

    # pohyb balonku 
    # v kazdou sekvenci se k aktualni pozici pripoji dva inkrementy
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #ODrazeni balonku od sten 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a += 1
        pen.clear()
        pen.write('PlayerA = {}  PlayerB = {}'.format(score_a,score_b), align='center', font=(('Courier',24,'normal')))

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1 
        score_b += 1
        pen.clear()
        pen.write('PlayerA = {} PlayerB = {}'.format(score_a,score_b), align='center', font=(('Courier',24,'normal')))      
    
    if ball.xcor() > 340 and (ball.ycor() < (paddle_b.ycor() +50) and ball.ycor() > (paddle_b.ycor() -50)):
        ball.dx*=-1
        ball.setx(340)
        winsound.PlaySound("augh.mp3", winsound.SND_ASYNC)
        
    if ball.xcor() < -340 and (ball.ycor() < (paddle_a.ycor()+50) and ball.ycor() > (paddle_a.ycor()-50)):
        
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("augh.mp3", winsound.SND_ASYNC)
    
        
 




