def testcase():
    # solution by anish0m
    try:
        a, b = map(int, input().split())
        print(int(a//b))
    except Exception as e:
        print("Error Code:", e)

    return



def main():
    t = int(input())
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
