from collections import defaultdict 

pathNodes = []  #list to store path in stack manner
class Graph():   
    def __init__(self, size): 
        self.size = size 
        self.vertices1={}
        self.graph = defaultdict(list)
    
    # Operation to add edge in graph using adjacency list
    def addEdge(self, src, dest, weight):  
        newNode = [dest, weight] 
        self.graph[src].insert(0, newNode)

    #Operation to print the result of MST  
    def printMSTEdges(self,dist,parent,n,startNode): 
        totalCost=0
        print("Edge\tCost")
        for i in range(n):
            if(self.getVal(i)!=startNode):
                print(self.getVal(i),"-",self.getVal(parent[i]),"\t",dist[i])
                totalCost+=dist[i]
        print("-------------------")
        print("Total MST Cost with start node ",startNode," is: ",totalCost)
    
    #Operation to print result of Dijktras algorithm
    def printShortestDistance(self,dist,parent,n,startNode):  
        pathString=""
        print("Vertex\tDistance\tPath")
        for i in range(n):            
            self.getShortestPath(parent,i) 
            for element in reversed(pathNodes):
                pathString+=element+" "
            print(self.getVal(i),"\t",dist[i],"\t\t",pathString)
            pathString=""
            pathNodes.clear()
    #Operation to get the shortest path from start node to each single node
    def getShortestPath(self, parent, j): 
        if parent[j] == -1 :
            pathNodes.append(self.getVal(j))
            return
        pathNodes.append(self.getVal(j))
        self.getShortestPath(parent , parent[j])        
    
    #Operation to get corresponding number of input alphabetical node
    def getNum(self,v):
        for x in self.vertices1:
            if x[1]==v:
                return x[0]
        return -1;
    
    #Operation to get corresponding input alphabetical node of the number
    def getVal(self,v):
        for x in self.vertices1:
            if x[0]==v:
                return x[1]
        return -1