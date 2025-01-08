def fibo(n):
    if n<=2:
        return 1
    return fibo(n-1)+fibo(n-2)
def listfibo(n):
    for i in range(1,n+1):
        print(fibo(i),end='\t')
n=int(input('Input n:'))
print(fibo(n))
listfibo(n)