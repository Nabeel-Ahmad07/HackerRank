cube = lambda x: x**3

def fibonacci(n):
    # Return a list of the first n Fibonacci numbers
    fibList = []
    a, b = 0, 1
    for _ in range(n):
        fibList.append(a)
        a, b = b, a + b
    return fibList

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))