if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0:
        if n in [2,3,4,5]:
            print("Not Weird")
        elif n >= 6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")