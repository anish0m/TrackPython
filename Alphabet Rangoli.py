# solution by anish0m



def print_rangoli(size):
    # your code goes here
    ch = chr(96+size)
    dn = (size-1)*2
    
    for i in range(1, size):
        b_dash = '-' * (dn)
        print(b_dash, end="")
        
        loop = size
        
        for j in range(size, size-i, -1):
            c = chr(96+j)
            loop = j
            
            print(c, end="")
            print("-", end="")
        
        loop +=1
        
        for j in range(loop, size+1, 1):
            c = chr(96+j)
            
            print(c, end="")
            print("-", end="")
        
        e_dash = '-' * (dn-1)
        print(e_dash, end="")
        
        dn -= 2
        print()
    
    print(ch, end="")
    
    for i in range(size-1, 0, -1):
        c = chr(96+i)
        
        print("-", end="")
        print(c, end="")
    
    for i in range(2, size+1, 1):
        c = chr(96+i)
        
        print("-", end="")
        print(c, end="")
    
    print()
    
    dn = 2
    
    for i in range(size, 1, -1):
        b_dash = '-' * (dn)
        print(b_dash, end="")
        
        loop = size
        
        for j in range(size, size-i+1, -1):
            c = chr(96+j)
            loop = j
            
            print(c, end="")
            print("-", end="")
        
        loop +=1
        
        for j in range(loop, size+1, 1):
            c = chr(96+j)
            
            print(c, end="")
            print("-", end="")
        
        e_dash = '-' * (dn-1)
        print(e_dash, end="")
        
        dn += 2
        print()

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)