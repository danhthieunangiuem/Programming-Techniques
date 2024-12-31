def H10ToH2(n):
    if n>0:
        remainder=n%2
        n=n//2
        H10ToH2(n)
        print(remainder,end='')
def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)
def list_fib(n):
    arr=[]
    for i in range(1,n+1):
        f=fib(i)
        arr.append(f)
    return arr
n=8
f8=fib(n)
arr8=list_fib(n)
print(f8)
print(arr8)
def move(n,A,B,C):
    if n==1:
        print(f'Move {A}=>{C}')
    else:
        move(n-1,A,B,C)
        print(f'Move {A}=>{C}')
        move(n-1,A,B,C)
n=3
move(3,'A', 'B','C')