
from math import sqrt

# task 1
def greet(name: str) -> str:
    print(f"Hello, {name}!!!")

def square(number):
    return number**2

def max_of_two(x, y):
    if x > y:
        return x
    return y

# task 2
def describe_person(name: str, age: int = 30) -> str:
    print(f"Имя: {name} Возраст: {age} лет")

# task 3
def is_prime(number: int) -> bool:
    for i in range(2, int(sqrt(number))+2):
        print(i)
        if number % i == 0:
            return False
    return True


        

