
numOfInp = input()
primeArray = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241]

# finding the x^a
def findA(N,prime):
    a = prime
    count = 0
    while N%a == 0:
        a *= prime
        count += 1
    return count


for i in range(int(numOfInp)):
    inpNum = int(input())
    N = inpNum
    sum = 1

    if inpNum == 1:
        print(0)
        continue
    if inpNum == 2:
        print(1)
        continue

    for pr in primeArray:
        if N%pr == 0:
            countx = findA(N,pr)
            s1 = ((pr**(countx+1)) - 1)/(pr-1)    
            N = N/(pr**countx)
            sum *= s1

    #if N by now is not 1, then it is surely a prime num
    if inpNum == N:
        sum = 1 + inpNum
    elif N != 1:
        sum *= (1 + N)
    
            
        
    sum = sum - inpNum
    print(int(sum))
