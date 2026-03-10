n = str(input())
high = 0
for i in range(len(n)):
    if int(n[i]) > int(high):
        high = str(n)[i]
print(high)