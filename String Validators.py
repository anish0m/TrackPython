# solution by anish0m



if __name__ == '__main__':
    s = input()
    
    flag = True
    temp = ""
    
    #line-1
    for i in range(len(s)):
        temp = s[i]
    
        if temp.isalnum():
            print("True")
            
            flag = False
            break

    if flag:
        print("False") 
    else:
        flag = True
    
    #line-2
    for i in range(len(s)):
        temp = s[i]
    
        if temp.isalpha():
            print("True")
            
            flag = False
            break

    if flag:
        print("False") 
    else:
        flag = True
    
    #line-3
    for i in range(len(s)):
        temp = s[i]
    
        if temp.isdigit():
            print("True")
            
            flag = False
            break

    if flag:
        print("False") 
    else:
        flag = True
    
    #line-4
    for i in range(len(s)):
        temp = s[i]
    
        if temp.islower():
            print("True")
            
            flag = False
            break

    if flag:
        print("False") 
    else:
        flag = True
    
    #line-5
    for i in range(len(s)):
        temp = s[i]
    
        if temp.isupper():
            print("True")
            
            flag = False
            break

    if flag:
        print("False") 
    else:
        flag = True
