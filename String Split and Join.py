# solution by anish0m



def split_and_join(line):
    # write your code here
    l = line.split(" ")
    s = "-".join(l)
    
    return s

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)