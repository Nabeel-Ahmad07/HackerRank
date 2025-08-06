def minion_game(string):
    # your code goes here
    kScore = 0
    sScore = 0
    
    vowels = "AEIOU"
    
    for i in range(len(string)):
        if string[i] in vowels:
            kScore += len(string)-i
        else:
            sScore += len(string)-i
                
    if sScore > kScore:
        print("Stuart", sScore)
    elif kScore > sScore:
        print("Kevin", kScore)
    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)