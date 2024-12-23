def testcase():
    # solution by anish0m
    l = int(input())  
    s1 = set(map(int, input().split()))
    N = int(input())

    for _ in range(N):
        op = input().split()[0]
        s2 = set(map(int, input().split()))

        if op == 'intersection_update':
            s1.intersection_update(s2)
        elif op == 'update':
            s1.update(s2)
        elif op== 'symmetric_difference_update':
            s1.symmetric_difference_update(s2)
        elif op == 'difference_update':
            s1.difference_update(s2)

    print(sum(s1))
    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
