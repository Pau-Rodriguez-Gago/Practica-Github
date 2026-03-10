ano=int(input())
if ano==2020:
    print("CANCELLED")
elif ano<2020 and ano>2014:
    print(ano-2014)
elif ano>2020 and ano<2025:
    print(ano-2015)
elif ano>2025:
    print("Coming soon.")
else:
    print("Did not exist.")