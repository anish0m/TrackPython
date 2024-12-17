def testcase():
    # solution by anish0m
    k = int( input() )
    rooms = list(map(int, input().split()))

    st = set(rooms)

    ans = sum(st) * k
    ans -= sum(rooms)
    ans //= (k-1)

    print(ans)
    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
