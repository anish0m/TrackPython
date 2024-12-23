# solution by anish0m



def count_substring(string, sub_string):
    count = 0
    start = 0
    
    while start < len(string):
        pos = string.find(sub_string, start)
        
        if pos == -1:
            break
            
        count += 1
        start = pos + 1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
