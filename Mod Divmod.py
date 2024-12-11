def testcase():
    # solution by anish0m
    a = int(input())
    b = int(input())

    print(a//b)
    print(a%b)
    print (divmod(a, b))

    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
