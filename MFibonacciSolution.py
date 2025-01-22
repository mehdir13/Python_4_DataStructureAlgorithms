import time

# Iterative Approach

def Fibonacci_iterative(n):
    f0, f1 = 0, 1
    for i in range(n):
        print(f0)
        # print (f0, end= "") to print the sequence in one line
        f0, f1 = f1, f0 + f1
    print (" ")


n_terms = int(input("How far would you wish Signore Fibonacci count his sequence for you?"))

start_time = time.time()
Fibonacci_iterative(n_terms)
Fibonacci_iterative_time = time.time() - start_time
print(f"Δt for the iteratibe approach to Fibonacci is: ", Fibonacci_iterative_time)
print("/././././././././././././././././././././././././././././././././")

# Recursive Approach

def Fibonacci_recursive(n):
    if n <= 1:
        return n
    return Fibonacci_recursive(n - 1) + Fibonacci_recursive(n - 2)

print(f"As you wished Signore Fibonacci counts his sequence for you to {n_terms}")

start_time = time.time()
for i in range(n_terms):
    print(Fibonacci_recursive(i))
    print(" ")
Fibonacci_recursive_time = time.time() - start_time
print(f"Δt for the recursive approach to Fibonacci is: ", Fibonacci_recursive_time)
print("/././././././././././././././././././././././././././././././././")

# My Best Approach

def fibonacci(n):
    f0 = 0
    f1 = 1
    
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return f0
    elif n == 1:
        return f1
    else:
        for i in range(1, n):
            fn = f0 + f1
            f0 = f1
            f1 = fn
        return f1

print(f"As you wished Signore Fibonacci counts his sequence for you to {n_terms}")

start_time = time.time()
print(fibonacci(n_terms))
fibonacci_time = time.time() - start_time
print(f"Δt for the recursive approach to Fibonacci is: ", fibonacci_time)
print("/././././././././././././././././././././././././././././././././")
