def calculate_love_score(name1, name2):
    string=name1+name2
    first="True"
    second="Love"
    nb1=0
    nb2=0
    for letter in first.lower():
        for le in string.lower():
            if letter==le:
                nb1 +=1
    for letter in second.lower():
        for le in string.lower():
            if letter==le:
                nb2 +=1
    nb=str(nb1)+str(nb2)
    print(nb)
    
    
calculate_love_score("Kanye West", "Kim Kardashian")