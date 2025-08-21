import time

def fib(n):
    if n==0 or n==1:
        return 1
    return fib(n-1) + fib(n-2)

def fib_loop(n):
    t1, t2 = 0, 1
    for _ in range(n):
        s = t1 + t2
        t1, t2 = t2, s
    return t2

t1 = time.time()
print(fib(35))
t2 = time.time()
print(t2 - t1)


t1 = time.time()
print(fib_loop(35))
t2 = time.time()
print(t2 - t1)
