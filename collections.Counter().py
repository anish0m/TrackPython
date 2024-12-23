from collections import Counter



def testcase():
    # solution by anish0m
    x = int(input())
    ls = Counter(map(int, input().split()))
    n = int(input())

    cash = 0

    for _ in range(n):
        s, r = map(int, input().split())
        
        if ls[s]: 
            ls[s] -= 1
            cash += r
            
    print(cash)
    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
