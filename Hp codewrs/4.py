attack = input().split(' ')
ball = input().split(' ')
defend = input().split(' ')
a = attack[0]
b = ball[0]
d = defend[0]
if int(a) > int(b) and int(a) > int(d):
    print('OFFSIDE')
else:
    print('GOAL')
