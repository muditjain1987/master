import sys
import queue

def dsf(G,strtNode,alreadyVisited,rs):

    if strtNode in alreadyVisited:
        return rs
    else:
        rs += str(strtNode) + " "
        alreadyVisited.append(strtNode)

    if strtNode in G:
        neigbours = G[strtNode]
        for n in neigbours:
            rs = dsf(G,n,alreadyVisited,rs)

    return rs    
    

def bsf(G,alreadyVisited,que,rs):

    if que.empty():
        return rs

    node = que.get()
    rs += str(node) + " "
    #print(node)
    neigbours = G[node]
    for n in neigbours:
        if n in alreadyVisited:
            www = 0
        else:
            que.put(n)
            alreadyVisited.append(n)
            
    rs = bsf(G,alreadyVisited,que,rs)
    return rs
    

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

            rs = ""
            if algo == 0:
                rs = dsf(G,q,alreadyVisited,rs)
                print(rs)
            else:
                que = queue.Queue()
                que.put(q)
                alreadyVisited.append(q)
                rs = bsf(G,alreadyVisited,que,rs)
                print(rs)
            q,algo = map(int,sys.stdin.readline().split())



main()
