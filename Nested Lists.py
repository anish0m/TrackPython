# solution by anish0m



if __name__ == '__main__':
    students=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])
    
    sortG = sorted(set([s[1] for s in students]))
    low2G = sortG[1]
    sort2N = sorted(set([s[0] for s in students if s[1]==low2G]))
    
    for n in sort2N:
        print(n)
