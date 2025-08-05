def print_rangoli(size):    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    width = 4*size-3
    r = []
    
    for i in range(size):
        s = "-".join(alpha[size-1:i:-1] + alpha[i:size])
        r.append(s.center(width, "-"))

    print('\n'.join(r[::-1] + r[1:]))

    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)