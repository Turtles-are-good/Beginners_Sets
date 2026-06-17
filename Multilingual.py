people = int(input("How many people are there: \n"))
lan = set()
every = None
for i in range( 1, people + 1) :
    numlan = int(input(f"\n How much languages does {i} person speak: \n"))
    lanlan = set()
    print("What languages can you speak")
    for d in range(numlan) :
        lang = input().lower()
        lanlan.add(lang)
    lan.update(lanlan)
    if every is None :
        every = lanlan
    else :
        every = every.intersection(lanlan)
print(f"\n The number of languages everyone can speak together is {len(every)}")
print(f"The languages everyone can speak is {every}")
print(f"Total languages spoken in the group is {len(lan)}")
print(f"Languages spoken {lan}")