def fib():
    print('fibonacci series')
    a,b = 0,1
    while 1:
        yield a
        a,b = b, a+b

a = fib()
print(a)
for _ in range(10):
    print(next(a))

