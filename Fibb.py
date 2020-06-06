m=1000000000000
def fib(n):
    a,b=1,1
    while a<n:
        print(str(a))
        a,b=b,a+b
fib(m)