if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    randList = list(arr)    
    largest = max(randList)
    newList = [x for x in randList if x != largest]
    runnerup = max(newList)
    print(runnerup)