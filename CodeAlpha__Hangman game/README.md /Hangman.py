import random
print("1.(fruits)")
print("2.(animals)")
print("3.(birds)")
print("4.(vegetables)")
choice = input("enter you choice(1/2/3/4):")
if choice=="1":
    words=["banana","apple","orange","pineapple","mango","pomogranate"]
elif choice=="2":
    words=["lion","tiger","deer","monkey","dog","donkey","hippo","zebra"]
elif choice=="3":
    words=["parrot","sparrow","crow","eagle"]
elif choice=="4":
    words=["cucumber","jinger","brinjal","cabbage","carrot","capsicum","little finger","snake guard","potato"]
else:
    print( "invalid" )
word = random.choice(words)
guess=[]
chances=6
while chances>0:
    display =""
    for i in word:
        if i in guess:
            display +=i
        else:
            display +="_"
            
    print(display)
    if display == word:
        print("you are win")
        break
    letter=input("enter letter:")
    guess.append(letter)
    if letter not in word:
        chances-=1
        print("wrong")
        print("left:",chances)
if chances==0:
        print("you lose the game,the word is:",word)


