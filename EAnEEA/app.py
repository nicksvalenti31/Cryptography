print("Enter two non-negative integers A and B (A must be greater than or equal to B)")
a,b= map(int, input().split())
x,y=a,b

while b>0:
    print(f'({a}, {b})')
    print(f'({b}, {a} mod {b})')
    m=a%b
    a=b
    b=m
print(f"gcd({x},{y})={a}")
