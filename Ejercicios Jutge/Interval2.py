#Write a program that, given two intervals, tells if one is inside the other. Input Input consists of four integer numbers a 1 , b 1 , a 2 , b 2 that represent the intervals [ a 1 , b 1 ] and [ a 2 , b 2 ] . Assume a 1 ≤ b 1 and a 2 ≤ b 2 . Output Print ‘=’ if the intervals are equal, ‘1’ if the first is inside the second (but they are not equal), ‘2’ if the second is inside the first (but they are not equal), or ‘?’ otherwise.
intervalos=input()
intervalos=intervalos.split()
a1=int(intervalos[0])
b1=int(intervalos[1])
a2=int(intervalos[2])
b2=int(intervalos[3])