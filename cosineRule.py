import math
def main():
    a = int(input("Enter a: "))  # int() function converts string to integer
    b = int(input("Enter b: "))  # int() function converts string to integer
    c = int(input("Enter c: "))  # int() function converts string to integer

    x = (((a**2)+(b**2)-(c**2))/(2*b*a))

    t = math.acos(x)
    
    

    y = math.degrees(t)

    print("The angle between a and b is: ", y)

    x3 = (((c**2)+(b**2)-(a**2))/(2*c*b))

    t3 = math.acos(x3)

    y3 = math.degrees(t3)

    print("The angle between b and c is: ", y3)

    x2 = (((a**2)+(c**2)-(b**2))/(2*c*a))

    t2 = math.acos(x2)

    y2 = math.degrees(t2)

    print("The angle between c and a is: ", y2)
main()

