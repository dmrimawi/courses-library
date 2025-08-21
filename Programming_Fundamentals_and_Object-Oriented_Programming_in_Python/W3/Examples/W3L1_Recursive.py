# Factorial
# n! 

def fact_loops(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = fact * i
    return fact

print(fact_loops(3))
print(fact_loops(2))
print(fact_loops(1))
print(fact_loops(0))

# Factorial stop: (n <= 1) -> 1
# fact(n) = n * fact(n-1)
# fact(n-1) = n-1 * fact(n-2) ... fact(1 OR 0)
print("_" * 50)
def fact_rec(n):
    if n <= 1:
        return 1
    return n * fact_rec(n-1)
print(fact_rec(3))
print(fact_rec(2))
print(fact_rec(1))
print(fact_rec(0))

# 24
# 	4 * 6
# 		    3 * 2
# 				2 * 1
					   
