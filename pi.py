def series(n):
    x = 0
    c = 1
    total = 0
    for i in range(n):
        c = (1 + (2 * i))
        flip = (-1) ** i
        newC = c*flip
        x = (4/newC)
        total = total + x
    return total
             
def main():
    print("Program that estimates Pi")
    times = eval(input("n? "))
    s = series(times)
    print("Approximation of Pi= ",s)
main()
