from graphics import *
import time

def main():
    win = GraphWin("Lab04", 400,400)
    win.setCoords(0, 0, 400, 400)
    cir = Circle(Point(100,50),40)
    rect = Rectangle(Point(300,300),Point(350,350))

    
    
    entry1 = Text(Point(100,50),"Circle")
    entry2 = Text(Point(325,325),"Square")

    win.getMouse()
    
    cir.setFill("red")
    rect.setFill("blue")
    cir.draw(win)
    rect.draw(win)
    entry1.draw(win)
    entry2.draw(win)

    win.getMouse()
    
    for i in range(100):
        rect.move(-3.25,0)
        cir.move(3.00,0)
        entry1.move(3.00,0)
        entry2.move(-3.25,0)
        time.sleep(.02)
        
    win.getMouse()
    
    
    

    
    
main()

    
                     
    
    
    
