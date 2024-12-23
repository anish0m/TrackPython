# solution by anish0m



import math

def print_formatted(number):
    # your code goes here
    b_num = bin(number)[2:]
    b_dig = len(b_num)
    
    for n in range(1, number+1):
        o = oct(n)[2:]
        h = hex(n)[2:].upper()
        b = bin(n)[2:]
        
        n_d_dig = len(str(n))
        n_o_dig = len(o)
        n_h_dig = len(h)
        n_b_dig = len(b)
        
        sp_n = ' ' * (b_dig - n_d_dig)
        sp_o = ' ' * (b_dig - n_o_dig)
        sp_h = ' ' * (b_dig - n_h_dig)
        sp_b = ' ' * (b_dig - n_b_dig)
        
        print(sp_n, end="")
        print(n, end="")
        
        
        print(sp_o, end=" ")
        print(o, end="")
        
        
        print(sp_h, end=" ")
        print(h, end="")
        
        
        print(sp_b, end=" ")
        print(b, end="")
        
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)