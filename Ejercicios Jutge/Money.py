money_tot=(input("")).split()
euros=int(money_tot[0])
cents=int(money_tot[1])
billetes_500=euros//500
resto_bil_500=euros%500
billetes_200=resto_bil_500//200
resto_bil_200=resto_bil_500%200
billetes_100=resto_bil_200//100
resto_bil_100=resto_bil_200%100
billetes_50=resto_bil_100//50
resto_bil_50=resto_bil_100%50
billetes_20=resto_bil_50//20
resto_bil_20=resto_bil_50%20
billetes_10=resto_bil_20//10
resto_bil_10=resto_bil_20%10
billetes_5=resto_bil_10//5
resto_bil_5=resto_bil_10%5
moneda_2=resto_bil_5//2
resto_mon_2=resto_bil_5%2
moneda_1=resto_mon_2//1
resto_mon_1=resto_mon_2%1
fifty_cents=cents//50
resto_50_cents=cents%50
twenty_cents=resto_50_cents//20
resto_20_cents=resto_50_cents%20
ten_cents=resto_20_cents//10
resto_10_cents=resto_20_cents%10
five_cents=resto_10_cents//5
resto_5_cents=resto_10_cents%5
two_cents=resto_5_cents//2
resto_2_cents=resto_5_cents%2
one_cent=resto_2_cents//1
resto_1_cent=resto_2_cents%1
print("Banknotes of 500 euros:", billetes_500)
print("Banknotes of 200 euros:", billetes_200)
print("Banknotes of 100 euros:", billetes_100)
print("Banknotes of 50 euros:", billetes_50)
print("Banknotes of 20 euros:", billetes_20)
print("Banknotes of 10 euros:", billetes_10)
print("Banknotes of 5 euros:", billetes_5)
print("Coins of 2 euros:", moneda_2)
print("Coins of 1 euro:", moneda_1)
print("Coins of 50 cents:", fifty_cents)
print("Coins of 20 cents:", twenty_cents)
print("Coins of 10 cents:", ten_cents)
print("Coins of 5 cents:", five_cents)
print("Coins of 2 cents:", two_cents)
print("Coins of 1 cent:", one_cent)
#Este ejercicio puede parecer una burrada pero es lo que mejor se me ocurrió, 
#dividia el dinero entre lo más grande y luego el resto entre lo siguiente más grande y así sucesivamente.