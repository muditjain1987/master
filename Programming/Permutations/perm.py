import sys

def perm(inpA,index):

    #print("Call" + str(inpA)+ " " + str(index))

    if index == (len(inpA) - 1):
        print(inpA)
        return


    for x in range(index,len(inpA)):
        if x == index :
            
            #recurse
            inpCpy = inpA[:]
            perm(inpCpy,index+1)
            
        else:
            #swap and recurse
            inpCpy = inpA[:]
            temp = inpCpy[index]
            inpCpy[index] = inpCpy[x]
            inpCpy[x] = temp
            #print(inpA)
            #print("Calling" + str(inpCpy))
            perm(inpCpy,index+1)
        
def main():

    #enter a string
    inp = sys.stdin.readline()
    inpArr = list(inp.strip())

    print(len(inpArr))
    #find all the permutations
    perm(inpArr,0)





main()
