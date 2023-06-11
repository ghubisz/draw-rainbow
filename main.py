import turtle

#creating a turtle screen object
sc = turtle.Screen()

#creating a turtle object(pen)
pen = turtle.Turtle()

#definining a method to form a semicircle with a dynamic radius and color
def semi_circle(col, rad, val):

    #set the fill color of the semicircle
    pen.color(col)

    #draw a circle
    pen.circle(rad, -180)

    #move the turtle to air
    pen.up()

    #move the turtle to a given position
    pen.setpos(val,0)

    #move the turtle to the ground
    pen.down()
    
    pen.right(180)

#set the colors for drawing
col = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

#setup the screen features
sc.setup(600,600)

#set the screen color to black
sc.bgcolor('black')

#setup the turtle features
pen.right(90)
pen.width(10)
pen.speed(7)

#loop to draw 7 semicircles
for i in range(7):
    semi_circle(col[i], 10 *(
        i +8), -10 * (i +1))
    
#hide the turtle
pen.hideturtle()