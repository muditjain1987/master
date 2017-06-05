import sys
import queue

def dsf(G,strtNode,alreadyVisited):

    #rs += str(strtNode) + " "
    sys.stdout.write(str(strtNode))
    sys.stdout.write(" ")
    alreadyVisited.append(strtNode)

    neigbours = G[strtNode]
    for n in neigbours:
        if n in alreadyVisited:
            www = 0
        else:
            dsf(G,n,alreadyVisited)

        
def bsf(G,strtNode):

    que = queue.Queue()
    alreadyVisited = []
    
    que.put(strtNode)
    alreadyVisited.append(strtNode)

    while que.empty() != True:

        node = que.get()
        #rs += str(node) + " "
        sys.stdout.write(str(node))
        sys.stdout.write(" ")
        #print(node)
        neigbours = G[node]
        for n in neigbours:
            if n in alreadyVisited:
                www = 0
            else:
                que.put(n)
                alreadyVisited.append(n)
        
    

def main():

    numOfGraphs = int(sys.stdin.readline())
    for t in range(1,(numOfGraphs+1)):

        G = {}
        numOfVertices = int(sys.stdin.readline())
        for n in range(1,(numOfVertices+1)):
            
            adjTuple = list(map(int,sys.stdin.readline().split()))
            G[adjTuple[0]] = adjTuple[2:]

        q,algo = map(int,sys.stdin.readline().split())
        print("graph " + str(t))
        while 1:
            alreadyVisited = []

            if q == 0 & algo == 0:
                break;

            if algo == 0:
                dsf(G,q,alreadyVisited)
                sys.stdout.write("\n")
                #print(rs.strip())
            else:
                bsf(G,q)
                sys.stdout.write("\n")
                #print(rs.strip())
            q,algo = map(int,sys.stdin.readline().split())



main()
