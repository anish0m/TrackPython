# solution by anish0m



cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    ls = [0, 1]

    for _ in range(2, n):
        ls.append(ls[-1] + ls[-2])
    
    return ls
    
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))