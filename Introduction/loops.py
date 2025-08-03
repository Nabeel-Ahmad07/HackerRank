if __name__ == '__main__':
    n = int(input())
    
    randomList = []
    
    for i in range(n):
        randomList.append(i)
        
    for j in randomList:
        print(j*j)