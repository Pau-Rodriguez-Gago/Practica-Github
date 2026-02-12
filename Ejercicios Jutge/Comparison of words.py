words=input("").split()
word1=words[0]
word2=words[1]
if word1<word2:
    print(word1,"<",word2)
elif word1>word2:
    print(word1,">",word2)
else:
    print(word1,"=",word2)