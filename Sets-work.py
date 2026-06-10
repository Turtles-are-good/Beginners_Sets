word = input("Enter a word or number \n")
a = set(word)
limit = int(input("How much letters do you want to remove? \n"))
count = 0
if limit > 0 :
    while limit > count :
        phrase = input("Enter a letter to remove \n")
        a.discard(phrase)
        count += 1
else :
    print("Enter a correct limit")
print(f"Your set is: \n {a}")