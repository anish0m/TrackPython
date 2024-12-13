def testcase():
    # solution by anish0m
    n = int(input())

    country = set()

    for i in range(n):
        country.add(input())

    print(len(country))
    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
