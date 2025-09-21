def factorial(n):
    value = int(input("Enter a number: "))
    for i in range(1, n):
        value *=i
    return value

print("Factorial of 5 is:", factorial(5))