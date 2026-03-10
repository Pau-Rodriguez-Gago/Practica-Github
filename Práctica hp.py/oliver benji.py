oliver=input().split()
benji=input().split()
si=0
for i in range(len(oliver)):
    if int(oliver[i])>int(benji[i]):
        si+=1
print(si)