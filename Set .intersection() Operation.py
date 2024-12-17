def testcase():
    # solution by anish0m
    n = int(input())
    english = set(map(int, input().split()))

    b = int(input())
    french = set(map(int, input().split()))
    
    st = english.intersection(french)
    
    print(len(st))
    return


def main():
    t = 1
    for _ in range(t):
        testcase()


if __name__ == "__main__":
    main()
