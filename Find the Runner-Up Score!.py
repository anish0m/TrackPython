# solution by anish0m



if __name__ == '__main__':
    if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    scores = set(arr)
    sortScore = sorted(scores, reverse=True)
    
    print(sortScore[1])