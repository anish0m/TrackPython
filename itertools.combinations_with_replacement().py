import itertools



def testcase():
    # solution by anish0
    s, n = input().split()

    C = list(itertools.combinations_with_replacement(sorted(s), int(n)))

    ls = [ ''.join(c) for c in C ]

    for x in ls:
        print(x)
    
    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
