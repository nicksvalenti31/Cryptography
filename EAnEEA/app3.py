import math
def eea(a, b, x1 = 1, x2 = 0, y1 = 0, y2 = 1):
    #a & b are entered values
    #X & Y values/coefficients; there are two values for each to allow for temporary values

	quotient = math.floor(a/b)
	remainder = a - quotient * b
	x3 = x1 - quotient * x2
	y3 = y1 - quotient * y2

    exists=True if b == 1 else exists=False

    #if remainder=0 gcd, X coefficient, Y coefficient will be printed
	return (b, x2, y2) if (remainder == 0) else eea(b, remainder, x2, x3, y2, y3)



print("Enter two non-negative integers A and B (A must be greater than or equal to B)")
a,b= map(int, input().split())

enteredresult=eea(a,b)
print("b, X, Y")
print(enteredresult)
