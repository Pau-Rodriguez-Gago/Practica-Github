año=int(input(""))
if año%4==0 and not (año%100==0) or (año%100==0 and año%400==0):
    print("YES")
else: 
    print("NO")
#Este fue muy sencillo, solo comprové si era bisiesto y cumplia con lo que se decía en el enunciado o no.