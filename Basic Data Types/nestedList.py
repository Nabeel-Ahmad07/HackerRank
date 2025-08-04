if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        randList = [name, score]
        students.append(randList)
    
    scores = [student[1] for student in students]
    
    smallest = min(scores)
    secondLast = min([x for x in scores if x != smallest])
    
    names = sorted([name[0] for name in students if name[1] == secondLast])
    for name in names:
        print(name)
