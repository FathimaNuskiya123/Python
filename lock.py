from random import randrange
import string
import random
from graphics import * 

class Lock: 
    def _init_(self):

        self.password = 'LOCK'
        self.errMsg = ''
        self.status = 'New'
        self.drawInitLock()


    
    def drawInitLock(self):
        self.win = GraphWin('Resettable combination lock',500,500)
        self.win.setCoords(0, 0 , 500, 500)
        self.rect = Rectangle(Point(50, 100),Point(450,400))
        self.rect.setFill('Lavender')
        self.rect.draw(self.win)
        cir1 = Circle(Point(100,300), 40)
        cir2 = Circle(Point(200,300), 40)
        cir3 = Circle(Point(300,300), 40)
        cir4 = Circle(Point(400,300), 40)
        self.circles = [cir1, cir2, cir3, cir4]
        for cir in self.circles:
            cir.setFill('Pink')
            cir.draw(self.win)

        text1 = Text(Point(100,300), 'L')
        text2 = Text(Point(200,300), 'O')
        text3 = Text(Point(300,300), 'C')
        text4 = Text(Point(400,300), 'K')
        self.texts = [text1, text2, text3, text4]
        for text in self.texts:
            text.setSize(20)
            text.draw(self.win)
        self.label = Text(Point(250, 200), self.status)
        self.label.setSize(20)
        self.label.draw(self.win)

    def updateTexts(self,value):
        text1 = updateTexts(self,1)
        text2 = updateTexts(self,2)
        text3 = updateTexts(self,3)
        text4 = updateTexts(self,4)





    
    def updateLabel(self):
        text1 = updateLabel(self.status,self.errMsg)
        text2 = updateLabel(self.status,self.errMsg)
        text3 = updateLabel(self.status,self.errMsg)
        text4 = updateLabel(self.status,self.errMsg)
        

    

    def close(self):
        text1 = random.choice(string.ascii_letters)
        text2 = random.choice(string.ascii_letters)
        text3 = random.choice(string.ascii_letters)
        text4 = random.choice(string.ascii_letters)
        self.label = Text(Point(250,200),self.status = "Closed")


    def open(self,password):
        if password is Lock:
            y = reset(self,password)
        else:
            y = close(self)

        


        
    def reset(self,password):
        if self.password < 4:
            self.label = Text(Point(250,200), "Password length should be 4")
            self.label.setSize(20)
            self.label.draw(self.win)
        else:
            self.label = Text(Point(250,200),self.status = "Reset")
            self.label.setSize(20)
            self.label.draw(self.win)
        x = updateLabel(self)
        
        


  
        
    def main():
        while(True):
        
            lock = Lock()
 
        
            password = input('\nPlease enter a new password to reset: ')
            while not lock.reset(password):
                password = input('\nPlease enter a new password to reset: ')
 
        
            answer = input('\nWant to play with the lock you just created? (yes/no) ')
            if answer.lower() == 'yes':
                lock.close()
 
                attempt = input("\nPlease enter the password to open: ")
                count = 0
                while not lock.open(attempt):
                    count += 1
                    if count < 3:           
                        print('\nYou only have ' + str(3-count) + ' chances left to enter password.')
                        attempt = input("Try again: ")            
                    else:
                        print('\nYou have failed 3 times! You cannot open it anymore!')
                        break
 
        
            answer = input('\nWant to play with a new lock?(yes/no) ')
            if answer.lower() == 'no':
                lock.win.close()
                break
            else:
                lock.win.close()           
    
 
    main()
