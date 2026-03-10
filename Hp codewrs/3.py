nights = int(input())
precio = int(input())
total = precio
for i in range(nights - 1):
    total += (0.9 * precio)
print(int (total) // 1)