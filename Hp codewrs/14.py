introducido = input().split(' ')
spam=['sale', 'sa1e', 's4le', 'sal3', '5ale', '5a1e', 's4l3', '5al3', 'SALE', 'SALe', 'SAle', 'Sale', 'sALE', 'sALe', 'SaLe', 'saLe', 'saLE', 'salE', 'sAle', '']
mayus = 'AEIOU'
spamP = False
contadorpau = 0
for i in introducido:
    lista = []
    contadorpau += 1
    for x in range(len(introducido[contadorpau - 1])):
        palabra = ''
        lista.append(i[x])
        for j in lista:
            if str(j).isalpha():
                str(j).lower()
                palabra += j
            else:
                palabra+=j
    if palabra in spam:
        spamP = True

if spamP:
    print('Email flagged as spam.')
else:
    print('Email appears legitimate.')