hi = []
words = set()
e = int(input("Enter how much numbers you want to input in your list: \n"))
i = 0
while i < e :
    word = int(input("Enter a number to be put in your list: \n"))
    hi.append(word)
    i += 1
for s in hi :
    if s in words :
        print("Yes")
    else :
        print("No")
        words.add(s)