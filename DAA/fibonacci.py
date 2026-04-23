def fibonacci(n):
    a, b = 0, 1
    steps = 0

    print("Fibonacci series:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
        steps += 1   

    print("\nTotal steps:", steps)


n = int(input("Enter the value of n for Fibonacci: "))
fibonacci(n)