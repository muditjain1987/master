import sys



def LCSarr(lenx,leny):

    aLCS = []

    for i in range(0,lenx+1):
        aLCS.append([])
        for j in range(0,leny+1):
            aLCS[i].append(0)

    return aLCS

def printLCS(aLCS,lenx,leny):

    for i in range(0,lenx+1):
        for j in range(0,leny+1):
            print(aLCS[i][j])
    


def findLCS(aLCS,X,Y):
    lenx = len(X)
    leny = len(Y)

    #print(X)
    #print(Y)
    
    indi = 0
    for i in range(1,lenx+1):
        indj = 0
        for j in range(1,leny+1):
            if X[indi] == Y[indj]:
                aLCS[i][j] = aLCS[i-1][j-1] + 1
            else:
                aLCS[i][j] = max(aLCS[i][j-1],aLCS[i-1][j])

            indj = indj + 1

        indi = indi + 1

    #printLCS(aLCS,lenx,leny)
    numOfLettersToMakePalin = lenx - aLCS[lenx][leny]    
    return numOfLettersToMakePalin


    
def main():
    
    #enter a string
    numOfInp = int(sys.stdin.readline())
    for i in range(int(numOfInp)):
        inp = sys.stdin.readline()
        X = list(inp.strip())
        Y = X[:]
        X.reverse()
        counter = findLCS(LCSarr(len(Y),len(X)),Y,X)
        print(counter)
    
       
main()
