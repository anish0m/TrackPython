def testcase():
    #solution by anish0m
    n = int(input(""))
    english = set(map(int , input("").split(" ")))
    
    b = int(input(""))
    french=set(map(int , input("").split(" ")))
    
    st = set(english.union(french))
    output = 0
    
    for _ in st:
        output+=1

    output = str(output)
    
    print(output)
    return



def main():
    t = 1 
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
