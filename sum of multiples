# Problem 1 - sum of multiples
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23. Find the sum of all the multiples of 3 and 5 below 1000.

def mult(x,y):
        sumThree = 0
        sumFive = 0
        sumFifteen = 0
        for i in range(1,1000):
            a = x*i
            b = y*i
            c = x*y*i
            if 0<a<1000:
                sumThree = sumThree+a
            if 0<b<1000:
                sumFive = sumFive+b
            if 0<c<1000:
                sumFifteen = sumFifteen+c
        print((sumThree+sumFive)-sumFifteen)        
mult(3,5)
