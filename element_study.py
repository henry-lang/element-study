from random import choice, randint
import os

try:
    from colors import color
except ImportError:
    print("Installing ansicolors")
    os.system("python3 -m pip install ansicolors -q")

elements = []
with open("elementlist.csv", "r") as f:
    elements = list(map(lambda l: l.strip().split(","), f.readlines()))

while True:
    element = choice(elements)
    front_or_back = randint(0, 1)
    answer = input(element[front_or_back] + ": ").lower()
    correct = element[abs(front_or_back - 1)]
    print(color("Correct!", fg="green", style="bold") if correct.lower() == answer else color(f"Wrong! Right answer is {correct}", fg="red", style="bold"))