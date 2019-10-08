cube = lambda x: x**3

def fibonacci(n):
    return [calculate_fibonacci(x) for x in range(n)]

def calculate_fibonacci(n):
    if n == 0 : 
        return 0
    elif n == 1 :
        return 1
    return calculate_fibonacci(n-2)+calculate_fibonacci(n-1)


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))