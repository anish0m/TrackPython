from collections import OrderedDict



def testcase():
    # solution by anish0m
    dc = OrderedDict()
    N = int(input())

    for n in range(N):
        item, space, price = input().rpartition(' ')
        dc[item] = dc.get(item, 0) + int(price)
        
    for item, price in dc.items():
        print(item, price)

    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
