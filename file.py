from math import tan, pi
import time

def decorator_function(func):
    def wrapper(*args, **kwargs):
        print('Была вызвана функция: {}'.format(func.__name__))
        first_time = time.time()
        func(*args, **kwargs)
        second_time = time.time()
        final_time = second_time - first_time
        print('Время затраченное на выполнение функции: {} секунд'.format(final_time))
    return wrapper

@decorator_function
def area(n, s):
    print((n * s**2) / (4 * tan(pi/n)))

@decorator_function
def sum_first_n(n):
    print((n * (n + 1))/2)

#Упражнение 1
n = int(input())
s = float(input())
area(n, s)

#Упражнение 2
n = int(input())
sum_first_n(n)