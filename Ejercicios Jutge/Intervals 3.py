a1, b1, a2, b2 = map(int, input().split())
if a1 == a2 and b1 == b2:
    relacion = '='
elif a1 >= a2 and b1 <= b2:
    relacion = '1'
elif a2 >= a1 and b2 <= b1:
    relacion = '2'
else:
    relacion = '?'
intersection_start = max(a1, a2)
intersection_end = min(b1, b2)
if intersection_start > intersection_end:
    intersection = "[]"
else:
    intersection = f"[{intersection_start},{intersection_end}]"

print(relacion, ",", intersection)
