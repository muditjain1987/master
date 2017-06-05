import sys
import math

def func(N):
    if inpNum == 1:
        return 0
    sum = 1
    upperBound = int(math.sqrt(N)) + 1
    for index in range(2,upperBound):
        if N % index == 0:
            if (index == N//index):
                sum += index
            else:
                sum += (N//index) + index
    return sum


numOfInp = int(sys.stdin.readline())
for i in range(int(numOfInp)):
    inpNum = int(sys.stdin.readline())
    print(func(inpNum))    
    
