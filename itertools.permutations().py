from itertools import permutations



def testcase():
    # solution by anish0
    s, n = input().split()

    for x in sorted(permutations(s, int(n))):
        print (''.join(x))

    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
