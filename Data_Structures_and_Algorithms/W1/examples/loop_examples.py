import time

def simple_loop(n):
    start = time.time()
    total = 0
    for i in range(1, n+1):
        total += i
    end = time.time()
    print("Total:", total)
    print("Time taken:", end - start, "seconds")

def constant(n):
    start = time.time()
    total = n * (n+1) / 2
    end = time.time()
    print("Total:", total)
    print("Time taken:", end - start, "seconds")

def naive(n):
    start = time.time()
    total = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            total += 1
    end = time.time()
    print("Total:", total)
    print("Time taken:", end - start, "seconds")

naive(100)
print("-" * 30)
simple_loop(100)
print("-" * 30)
constant(100)
print("-" * 60)
naive(10000)
print("-" * 30)
simple_loop(10000)
print("-" * 30)
constant(10000)
print("-" * 60)
naive(1000000)
print("-" * 30)
simple_loop(1000000)
print("-" * 30)
constant(1000000)

