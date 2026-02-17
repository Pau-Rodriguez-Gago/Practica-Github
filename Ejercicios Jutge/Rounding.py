#Write a program that reads a real number x ≥ 0 and prints ⌊ x ⌋ (the floor of x ), ⌈ x ⌉ (the ceiling of x ), and the rounding of x . Input Input consists of a real number x ≥ 0 . Output Print the floor of x , the ceiling of x , and the integer number closer to x ( ⌈ x ⌉ if there is a tie).
x=float(input(""))
import math
if x-math.floor(x)<math.ceil(x)-x:
    print(math.floor(x),math.ceil(x),math.floor(x))
elif x-math.floor(x)>math.ceil(x)-x:
    print(math.floor(x),math.ceil(x),math.ceil(x))
else:
    print(math.floor(x),math.ceil(x),math.ceil(x))