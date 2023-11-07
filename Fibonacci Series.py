def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Get the number of terms from the user
n = int(input("Enter the number of Fibonacci terms to generate: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(n)
    print("Fibonacci series up to {} terms:".format(n))
    print(result)
