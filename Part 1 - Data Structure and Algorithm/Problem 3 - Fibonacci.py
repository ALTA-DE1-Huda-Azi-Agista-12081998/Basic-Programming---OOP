def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input value for n
n = 10  # You can change this to any desired value

# Calculate and print the nth Fibonacci number
print(fibonacci(0))
print(fibonacci(2))
print(fibonacci(9))
print(fibonacci(10))
print(fibonacci(12))