def rubberbandedstar(t,d,c):
    t.begin_fill()
    t.color(c)
    for times in range(5):
        t.forward(200)
        t.right(144)
    t.end_fill()
    
def teleport(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()





