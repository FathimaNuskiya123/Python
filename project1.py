import math
def main():
    w = eval(input("Enter the Distance d1: "))
    x = eval(input("Enter the Distance d2: "))
    h = eval(input("Enter the Height of the Stage : "))
    a = eval(input("Enter the angle of the ramp in degrees : "))
    c = math.radians(a)
    g = 9.8
    t = math.sqrt((2*h)/g)
    h = .5*g*(t**2)
    v = (w + x)/(2*t)

    print("It takes ", t, " seconds for the bird to hit the pig.")
    print("The bird must travel at a velocity of ", v)

    
    tt = math.sqrt(((2*h + math.tan(c)*(w+x))/g))
    vv = (w+x)/(2*(math.cos(c))*tt)

    print("It takes ", tt , "seconds for the bird to hit the pig when the bird is running on the ramp.")
    print("The bird must travel at a velocity of", vv , " when the bird is running on the ramp.")


main()

