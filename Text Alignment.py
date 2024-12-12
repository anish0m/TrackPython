def testcase():
    # solution by anish0m
    N = int(input())
    
    for n in range(1, N+1):
        h = 'H' * (2*n - 1)
        sp = ' ' * (N-n)

        print(sp + h + sp)
    
    h1 = 'H' * (N)
    h2 = 'H' * (3*N)

    ssp = ' ' * (N//2)
    lsp = ' ' * (3*N)

    for n in range(0,N+1):
        print(ssp + h1 + lsp + h1)

    n1 = (N+1) // 2

    for n in range(0,n1):
        print(ssp + h1 + h2+ h1)

    for n in range(0,N+1):
        print(ssp + h1 + lsp + h1)
    
    ind = ' ' * (4*N)

    for n in range(N, 0, -1):
        h= 'H' * (2*n - 1)
        sp= ' ' * (N-n)

        print(ind + sp + h + sp)
    
    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()