from itertools import product



def testcase():
    # solution by anish0m
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(*list(product(A, B)))
    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
