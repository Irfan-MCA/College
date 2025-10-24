#Program to find the factorial of a number using loops and also using recursion.
'''

def factorial_loop(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."

    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply result by i in each iteration

    return result

# Example usage
num = int(input("Enter a number: "))
print("Factorial using loop:", factorial_loop(num))




'''


def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1  # Base case
    else:
        return n * factorial_recursive(n - 1)  # Recursive call

# Example usage
num = int(input("Enter a number: "))
print("Factorial using recursion:", factorial_recursive(num))

