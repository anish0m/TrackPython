def testcase():
    # solution by anish0m
    n = int(input())
    columns = input().split()

    data = [input().split() for _ in range(n)]

    index = columns.index("MARKS")
    total = sum(float(t[index]) for t in data)
    avg = total / n

    print(f"{avg:.2f}")
    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
