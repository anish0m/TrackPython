# solution by anish0m



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    score = student_marks[query_name]
    avg = sum(score) / len(score)
    
    print(f"{avg:.2f}")