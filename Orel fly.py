import turtle,time,random
wn=turtle.Screen()
wn.setup(1200,700)
wn.bgpic('orel_background.gif')
turtle.tracer(5)
eagles=[0]
for i in range(1,22):
    i1=str(i)
    eagles.append('eagle'+i1+'.gif')
   
orel=turtle.Turtle()
orel.up()
orel.goto(600,0)
while True:
    orel.setheading(random.randint(-15,15))
    
    if orel.xcor()<-600:
        orel.goto(600,0)
               
    for i in range(1,22):
        wn.addshape(eagles[i])
        orel.shape(eagles[i])
        time.sleep(0.1)
        orel.fd(-10)
