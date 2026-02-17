letter=input("")
if letter.isupper():
    print("uppercase")
if letter.islower():
    print("lowercase")
if letter in "aeiouAEIOU":
    print("vowel")
if letter not in "aeiouAEIOU":
    print("consonant")
#Solo hay que usar islower y isupper como comprovaciones y luego ver si está en la lista de las vocales o no.