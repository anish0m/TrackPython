import calendar



def testcase():
    # solution by anish0m
    m, d, y = list(map(int,input().split()))
    D = calendar.weekday(y, m, d)

    print((calendar.day_name[D]).upper())
    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
