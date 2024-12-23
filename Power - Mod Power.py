def testcase():
    # solution by anish0m
    a = int(input())
    b = int(input())
    m = int(input())

    print(pow(a, b))
    print(pow(a, b, m))

    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
