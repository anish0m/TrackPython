def is_leap(year):
    leap = False
    
    # Write your logic here
    # solution by anish0m
    if not year%4:
        leap = True

        if not year%100:
            if not year%400:
                leap = True
            else:
                leap = False
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))