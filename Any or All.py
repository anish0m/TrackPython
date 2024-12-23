def isPalindrome(num):
    return num == num[::-1]



def testcase():
    # solution by anish0m
    N = int(input())
    arr = list(input().split())

    print(
        all(int(x) >= 0 for x in arr)
        and any(isPalindrome(x) for x in arr)
    )

    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
