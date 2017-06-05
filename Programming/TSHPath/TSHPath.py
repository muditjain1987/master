import sys
from heapq import heappush
from heapq import heappop

def findShortestPathCost (src,dst,vertexCost,Graph,EdgeCost):

    startNodeIndex = src
    finalCost = 0
    q = []  #empty list

    
    vertexCost[startNodeIndex] = 0
    tupleToPush = (0,startNodeIndex,startNodeIndex)
    heappush(q, tupleToPush)
    #print("pushing:")
    #print(tupleToPush)

    visitedList = []
    
    #loop untill queue is empty    
    while q:

        popNodeCost,popSrcNode,popDestNode = heappop(q)

        visitedList.append(popDestNode)

        #print("popping")
        #print(popNodeCost)
        if popDestNode == dst:
            break
        
        neighbours = Graph[popDestNode]
        for n in neighbours:
            if n in visitedList:
                ds = 1
                #already visited do nothing
            else:
                newCost = (popNodeCost + EdgeCost[(popDestNode,n)])
                if vertexCost[n] > newCost:
                    vertexCost[n] = newCost
                    tupleToPush = (newCost,popDestNode,n) 
                    #print("pushing")
                    heappush(q,tupleToPush)
                    #print(tupleToPush)


    finalCost = vertexCost[dst]
    return finalCost


def main():

    numTests = int(sys.stdin.readline())
    for test in range(1,(numTests+1)):

        vertexCost = {} # vertexid : cost from src
        Vertices = {} # cityName: id
        Graph = {} # id: id1,id2
        EdgeCost = {} # 'id1 id2' : cost
        cityIndex = 1

        numCities = int(sys.stdin.readline())
        for city in range(1,(numCities+1)):

            cityName = sys.stdin.readline()
            Vertices[cityName] = cityIndex
            vertexCost[cityIndex] = 200001
            ConnectedCities = []
            Graph[cityIndex] = ConnectedCities

            numNeighbours = int(sys.stdin.readline())
            for neighbour in range(1,(numNeighbours+1)):

                index,cost = map(int,sys.stdin.readline().split())
                ConnectedCities.append(index)
                EdgeCost[(cityIndex,index)] = cost

            cityIndex += 1

        numOfPaths = int(sys.stdin.readline())
        for path in range(1,(numOfPaths+1)):
            src,dst = map(str,sys.stdin.readline().split())
            src += '\n'
            dst += '\n'
            for vert in vertexCost.keys():
                vertexCost[vert] = 200001

            print(findShortestPathCost(Vertices[src],Vertices[dst],vertexCost,Graph,EdgeCost))

        if test < numTests:
            sys.stdin.readline()


main()
