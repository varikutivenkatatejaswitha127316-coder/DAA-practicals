#iterative method

def factorial_iterative(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


n = int(input("Enter a number: "))
print("Factorial =", factorial_iterative(n))



#recursive method
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)

n = int(input("Enter a number: "))
print("Factorial =", factorial_recursive(n))
