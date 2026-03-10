letras = input()
salida = ''
for i in range(len(letras)):
    if letras[i] == '_':
        salida = salida + 'w'
    if letras[i] == 'G':
        salida = salida + 'fw'
    if letras[i] == 'E':
        salida = salida + 'ffw'
    if letras[i] == 'S':
        salida = salida + 'fffw'
    if letras[i] == 'T':
        salida = salida + 'ffffw'
print(salida)