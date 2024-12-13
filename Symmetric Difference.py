def testcase():
    # solution by anish0m
    M = int(input())
    set_m = set(map(int,input().split()))
    
    N = int(input())
    set_n = set(map(int,input().split()))
    
    m = (set_m.difference(set_n))
    n = (set_n.difference(set_m))
    
    res = m.union(n)
    
    for i in sorted(res):
        print (i)

    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
