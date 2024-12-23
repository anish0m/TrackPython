def testcase():
    #solution by anish0m
    n = int(input())
    st = list(map(int, input().split()))

    for _ in range(int(input())):
        s = input().split()
        
        if s[0] == 'pop':
            if st:
                st.pop(0)
        elif s[0] == 'remove':
            val = int(s[1])
            if val in st:
                st.remove(val)
        elif s[0] == 'discard':
            val = int(s[1])
            if val in st:
                st.remove(val)

    print(sum(st))
    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
