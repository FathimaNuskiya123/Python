from graphics import *
def Cipher_wheel():
    win = GraphWin("Wheel", 600, 600)
    win.setCoords(0,0,600,600)
    inner = Circle(Point(300,250), 200)
    outer = Circle(Point(300,250), 240)
    inner1 = Circle(Point(300,250),150)
    inner.setOutline("black")
    outer.setOutline("black")
    inner1.setOutline("black")
    inner1.draw(win)
    inner.draw(win)
    outer.draw(win)
    p1 = Point(60,250)
    p2 = Point(540,250)
    p3 = Point(300,490)
    p4 = Point(300,250)
    p5 = Point(300,10)
    
    Line1 = Line(p1,p2)
    Line2 = Line(p3,p4)
    Line3 = Line(p4,p5)
    Line1.draw(win)
    Line2.draw(win)
    Line3.draw(win)
    
    
    
    
Cipher_wheel()
