"""TO FIND AREA"""
a = input('Hi.i am your computer speaking.What is your name:')
print('Hello',a)
print('Nice to meet you')
print('You can use this program to calculate the area of different shapes')
s = input('Please enter the shape of which you want to find area of:')
if s == "Square": #||"square"|| "SQUARE"):
    t = float(input('Please the the side of the square:'))
    aq = t*t
    print('The area is',aq,'unit sq.')
elif s == "Rectangle": #||"rectangle"||"Reactangle";
    l = float(input('Please enter the length:'))
    b = float(input('Please enter the breadth:'))          
    ar = l*b
    print('The area is',ar,'unit sq.')
elif s == "Circle": #||"cirle"||"CIRCLE":
    r = float(input('Please the enter the radius:'))
    from math import *
    ac = pi*r*r
    print('The area is',ac,'unit sq.')
print('Thank you for using this program')

