modo = input()
hora = input().split(':')
sec_tot=0
min_fr=0
sec_fr=0
hor_fr=0
if modo == 'Metric':
    sec_tot+=int(hora[0])*3600
    sec_tot+=int(hora[1])*60
    sec_tot+=int(hora[2])
    sec_tot = sec_tot // 1,157407407407407
    hor_fr=float(sec_tot)//10000
    min_fr=(float(sec_tot)%10000)//100
    sec_fr=(float(sec_tot)%10000)%100
print(hor_fr)
print(min_fr)
print(sec_fr)