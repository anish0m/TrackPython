from collections import deque



def testcase():
    # solution by anish0m
    d = deque()

    for i in range(int(input())):
        command = input().split()
        
        if command[0] == 'append':
            d.append(command[1])
        elif command[0] == 'appendleft':
            d.appendleft(command[1])
        elif command[0] == 'pop':
            d.pop()
        else:
            d.popleft()
            
    print(' '.join(d))
    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
