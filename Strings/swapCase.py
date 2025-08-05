def swap_case(s):
    a = ""
    for char in s:
        if char.islower():
            char = char.upper()
        elif char.isupper():
            char = char.lower()
        
        a+=char
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)