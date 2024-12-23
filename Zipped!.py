def testcase():
    # solution by anish0m
    n, x = map(int, input().split())

    sheet = []
    
    for _ in range(x):
        sheet.append(map(float, input().split()))

    for i in zip(*sheet):
        print(sum(i) / len(i))  

    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
