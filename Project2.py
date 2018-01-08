from graphics import *
from math import *


def caesarEncipher(message, shift):
    message = message.upper()
    encipheredMessage = ""
    if(shift < 0):
        shift = 26 + shift
    for i in message:
        encipheredMessage += chr(((ord(i) - 65 + shift) % 26) + 65)
    
    return encipheredMessage



def caesarDecipher(message, shift):
    message = message.upper()
    decipheredMessage = ""
    if(shift < 0):
        shift = shift + 26
    
    for i in message:
        decipheredMessage += chr(((ord(i) - 65 - shift) % 26) + 65)
    
    return decipheredMessage

def Cipher_Wheel(message,cipher):
    
    messageLength = len(message)
    
    win = GraphWin("Cipher Wheel", 600 , 600)
    win.setBackground("yellow")
    innerCipherCircle = Circle(Point(300, 250), 200)
    outerMessageCircle = Circle(Point(300, 250), 240)
    extraCircle = Circle(Point(300, 250), 160)
    
    counter = 1;
    
    for n in range(0, messageLength):
            innerXCoord = (extraCircle.getRadius() * cos((2 * n * pi)/messageLength)) + 300
            innerYCoord = (extraCircle.getRadius() * sin((2 * n * pi)/messageLength)) + 250
            outerXCoord = (outerMessageCircle.getRadius() * cos((2 * n * pi)/messageLength)) + 300
            outerYCoord = (outerMessageCircle.getRadius() * sin((2 * n * pi)/messageLength)) + 250
            line = Line(Point(innerXCoord, innerYCoord), Point(outerXCoord, outerYCoord))
            
            line.draw(win)

            innerTextXCoord = (180 * cos((2 * counter * pi)/(messageLength*2))) + 300
            innerTextYCoord = (180 * sin((2 * counter * pi)/(messageLength*2))) + 250
            outerTextXCoord = (220 * cos((2 * counter * pi)/(messageLength*2))) + 300
            outerTextYCoord = (220 * sin((2 * counter * pi)/(messageLength*2))) + 250
            innerText = Text(Point(innerTextXCoord, innerTextYCoord), message[n])
            outerText = Text(Point(outerTextXCoord, outerTextYCoord), cipher[n])
            innerText.draw(win)
            outerText.draw(win)
            counter += 2

    innerCipherCircle.draw(win)
    outerMessageCircle.draw(win)
    extraCircle.draw(win)
    win.getMouse()
    win.close()


def main():
    
    
    message = input("Please input the message to encode: ")
    shift = int(input("Please input a shift value: "))
    
    caesarCipher = caesarEncipher(message, shift)
    print("CaesarCipher: %s" % caesarCipher)
    caesarDec = caesarDecipher(caesarCipher, shift)
    print("CaesarDec: %s" % caesarDec)
    Cipher_Wheel(caesarDec, caesarCipher)
    
main()
