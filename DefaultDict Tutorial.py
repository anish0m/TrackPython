from collections import defaultdict



def testcase():
    # solution by anish0m
    N, M = map(int, input().split())
    dc = defaultdict(list)

    for n in range(N):
        ans1 = input()
        dc[ans1].append(n+1)

    for m in range(M):
        ans2 = input()

        if ans2 in dc:
            print(*dc[ans2])
        else:
            print(-1)

    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
