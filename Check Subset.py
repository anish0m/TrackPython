def testcase():
    # solution by anish0m
    n = int(input())
	A = set(input().split())
    
	m = int(input())
	B = set(input().split())
	
	if len(A.difference(B)):
		print('False')
	else:
		print('True')

    return



def main():
    t = int( input() )
    for _ in range(t):
        testcase()



if __name__ == "__main__":
    main()
