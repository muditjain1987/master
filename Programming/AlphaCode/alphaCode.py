import sys


def IsTwoDigNumUseful(a,b):
    if (int(a) == 1) | (int(a) == 2 and int(b) <= 6):
        return True
    else:
        return False
    


def WrngDecodeCount(inpArr):

    result = []
    length = len(inpArr)
    j = 0

    for i in range(0,length):

        result.append(0)

        if (i < length-2) and (int(inpArr[i]) == 0 and int(inpArr[i+1]) == 0):
            return 0

        if (i > 1) and (int(inpArr[i]) == 0 and int(inpArr[i-1]) > 2):
            return 0

    
    for i in range(length-1,-1,-1):

        if j == 0:
            if int(inpArr[i]) >= 1 and int(inpArr[i]) <= 9:
                result[i] = 1
            else:
                result[i] = 0
            j = j+1
            continue

        if j == 1:
            if IsTwoDigNumUseful(inpArr[i],inpArr[i+1]):
                result[i] = result[i+1] + 1
            else:
                if int(inpArr[i]) == 0:
                    result[i] = 0
                else:
                    result[i] = result[i+1]
            j = j+1
            continue

        if IsTwoDigNumUseful(inpArr[i],inpArr[i+1]):
            result[i] = result[i+1] + result[i+2]
        else:
            if int(inpArr[i]) == 0:
                result[i] = 0
            else:
                result[i] = result[i+1]

    return result[0]

    
def main():
    #enter a string
    while(True):
        inp = sys.stdin.readline()
        inpArr = list(inp.strip())
        #print(inp.strip())
        if inp.strip() == '0':
            break

        counter = WrngDecodeCount(inpArr)
        print(counter)
        


main()
