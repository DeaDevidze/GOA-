from turtle import*

#we want to paint a house


width(7)
speed(5)
color("light blue")
begin_fill()
forward(200)
left(90)
end_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
# end of a scuare

#drawing a door

forward(70)
color("pink")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#roof
penup()
goto(200, 200)
pendown()

color("teal")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#add window

width(3)
penup()
goto(200, 150)
pendown()

color("plum")
begin_fill()
left(30)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#left window
penup()
goto(-1, 100)
pendown()

color("plum")
begin_fill()
left(90)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


exitonclick()