def testcase():
    # solution by anish0m
    A = set(input().split())
    n = int( input() )

    flag = True

    for x in range(0, n):
        sub_set = set(input().split())
        
        if len(sub_set.difference(A)):
            flag = False
            break

    if flag:
        print('True')
    else:
        print('False')

    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
