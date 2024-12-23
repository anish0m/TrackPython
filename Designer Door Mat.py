def testcase():
    # solution by anish0m
    N, M = map(int, input().split())
    
    m_dash = (M-7) // 2
    n_dash = m_dash + 2

    for n in range(N//2):
        dash = '-' * (n_dash)
        print(dash, end="")
        
        m1 = 2 * (n+1)
        
        for m in range(m1-1):
            print(".|.", end="")
        
        print(dash)
        n_dash -= 3
    
    dash = '-' * (m_dash)
    
    print(dash, end="")
    print("WELCOME", end="")
    print(dash, end="")
    
    n_dash += 3
    print()

    for n in range(N//2):
        dash = '-' * (n_dash)
        print(dash, end="")
        
        m1 =  N - (2*(n+1))
        
        for m in range(m1):
            print(".|.", end="")
        
        print(dash)
        n_dash += 3

    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
