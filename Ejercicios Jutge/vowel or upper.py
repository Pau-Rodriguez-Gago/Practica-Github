letter=input("")
if letter.isupper():
    print("uppercase")
if letter.islower():
    print("lowercase")
if letter in "aeiouAEIOU":
    print("vowel")
if letter not in "aeiouAEIOU":
    print("consonant")