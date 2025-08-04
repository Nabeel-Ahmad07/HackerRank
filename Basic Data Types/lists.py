if __name__ == '__main__':
    N = int(input())
    
    randList = []
    
    for _ in range(N):
        cmd = input().split()
        
        if cmd[0] == "insert":
            randList.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "remove":
            randList.remove(int(cmd[1]))
        elif cmd[0] == "append":
            randList.append(int(cmd[1]))
        elif cmd[0] == "sort":
            randList.sort()
        elif cmd[0] == "pop":
            randList.pop()
        elif cmd[0] == "reverse":
            randList.reverse()
        elif cmd[0] == "print":
            print(randList)
