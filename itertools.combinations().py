from itertools import combinations



def testcase():
    # solution by anish0
    s, n = input().split()

    for i in range(1, int(n)+1):
        for j in combinations(sorted(s), i):
            print (''.join(j))


    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
