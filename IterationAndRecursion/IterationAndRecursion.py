


def iterative_factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def recursive_factorial(n):
    if n==0:
        return 1
    else:
        return n * recursive_factorial(n-1)

numbers = [0,5,10,25,50,100]

print("Iterative Factorial Results:")
for num in numbers:
    print(f"{num}! = {iterative_factorial(num)}")
print("\nRecursive Factorial Results:")
for num in numbers:
    print(f"{num}! = {recursive_factorial(num)}")
    
