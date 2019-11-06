def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    str_lenght = len(string)
    kevin_score, stuart_score = 0, 0

    for i in range(str_lenght):
        if s[i] in vowels:
            kevin_score += (str_lenght - i)
        else:
            stuart_score += (str_lenght - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score,end="")
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score,end="")
    else:
        print("Draw",end="")
