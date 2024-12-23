# solution by anish0m



if __name__ == '__main__':
    N = int(input())
    ls= []
    
    for i in range(0, N):
        inp= input()
        l = inp.split()
        
        if l[0] == 'insert':
            ls.insert(int(l[1]), int(l[2]))
        elif l[0] == 'print':
            print(ls)
        elif l[0] == 'remove':
            ls.remove(int(l[1]))
        elif l[0] == 'append':
            ls.append(int(l[1]))
        elif l[0] == 'sort':
            ls.sort()
        elif l[0] == 'pop':
            ls.pop()
        elif l[0] == 'reverse':
            ls.reverse()
        else:
            pass
