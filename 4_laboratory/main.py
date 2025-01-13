import time
from math import sqrt

from my_module import sum2num
from Operations.numbers import sumTwoNum
from Operations.string import reverse

from .. import new

new.f()

def num_sqtrt(x) -> float:
    return round(sqrt(x), 2)

def current_date() -> str:
    return time.strftime("%d.%m.%Y")

print(f"\33]current date: {current_date()}")
print(f"sqrt of 225: {num_sqtrt(225)}")
print(f"sum 2 numbers: {sum2num(10, 40)}")
print(f"sum 2 numbers: {sumTwoNum(30, 20)}")
print(f"reverse string 'Hello': {reverse('Hello')}")