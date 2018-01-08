import math
def sum(a,r,n):
    geoSum = 0
    for i in range(1,n+1):
        geoSum = geoSum + (a*r**(i-1))
        termNum = (a*r**(i-1)) 
        print ("Term ", i, "= ", termNum)
 
    return geoSum
 
def main():
    print("Calculate the sum of geometric series")
    a = int(input("a? "))
    r = int(input("r? "))
    n = int(input("n? "))
    print("sum = ",sum(a, r, n))
 
main()
