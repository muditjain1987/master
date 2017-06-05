import queue

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
              5:99999}
EdgeCost = { '1 2': 20,
             '2 3': 30,
             '3 4': 40,
             '4 5': 50
           }

def findShortestPathCost (src,dst):

    startNodeIndex = src
    q = queue.Queue()
    q1 = queue.PriorityQueue()
    q.put(startNodeIndex)
    vertexCost[startNodeIndex] = 0
    finalCost = 0
    
    #loop untill queue is empty    
    while q.empty() == False:

        popNodeIndex = q.get()
        print(popNodeIndex)
        # src-src is 0 cost
        neighbours = Graph[popNodeIndex]
        for n in neighbours:
            vertexCost[n] = min(vertexCost[n], vertexCost[popNodeIndex] + EdgeCost[str(popNodeIndex) + " " + str(n)])
            q.put(n)


    finalCost = vertexCost[dst]
    return finalCost



print(findShortestPathCost(1,4))
