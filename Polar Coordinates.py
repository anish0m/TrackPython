import cmath



def testcase():
    # solution by anish0m
    z = complex(input().strip())

    r = abs(z)
    phi = cmath.phase(z)

    print(r)
    print(phi)

    return



def main():
    t = 1
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
