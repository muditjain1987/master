from heapq import heappush
from heapq import heappop


# graph dictionary shows the links between vertices
Graph = {
    1 : [2],
    2 : [3],
    3 : [4],
    4 : [5],
    5 : []
    }

vertexCost = {1:99999,
              2:99999,
              3:99999,
              4:99999,
              5:99999
              }

EdgeCost = { (1,2):20,
             (2,3):30,
             (3,4):40,
             (4,5):50
           }

def findShortestPathCost (src,dst):

    startNodeIndex = src
    finalCost = 0
    vertexCost[startNodeIndex] = 0

    q = []  #empty list
    heappush(q, (0,startNodeIndex,startNodeIndex))
    
    #loop untill queue is empty    
    while q:

        popNodeCost,popSrcNode,popDestNode = heappop(q)
    
        neighbours = Graph[popDestNode]
        for n in neighbours:
            vertexCost[n] = min(vertexCost[n], popNodeCost + EdgeCost[(popDestNode,n)])
            heappush(q,(vertexCost[n],popDestNode,n))


    finalCost = vertexCost[dst]
    return finalCost



print(findShortestPathCost(1,4))
