class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Node:
    def __init__(self, point, g = 0, h = 0):
        self.point = point         #self position 
        self.father = None         #father node
        self.g = g
        self.h = h

    
    # H use manhattan distance
    def setH(self, endNode):
        self.h = (abs(endNode.point.x - self.point.x) + abs(endNode.point.y - self.point.y))*10

    def setG(self):
        if abs(self.point.x - self.father.point.x) == 1 and abs(self.point.y - self.father.point.y) == 1:  
            gTmp = 14  
        else:  
            gTmp = 10 
        self.g = gTmp + self.father.g
    
    def setFather(self, node):
        self.father = node

class AStar:
    def __init__(self, map2d, startNode, endNode):
        # map2d      
        # startNode 
        # endNode   

        self.openlist = []
        self.closelist = []
        self.map = map2d
        self.startNode = startNode
        self.endNode = endNode
        self.currentNode = startNode
        self.pathlist = []
    
    def getMinFNode(self):
        # find the min F in openlist
        
        nodeTemp = self.openlist[0]
        for node in self.openlist:
            if node.g + node.h < nodeTemp.g + node.h:
                nodeTemp = node
        return nodeTemp

    def nodeInOpenlist(self, node):
        for nodetmp in self.openlist:
            if nodetmp.point.x == node.point.x \
            and nodetmp.point.y == node.point.y:
                return  True
        return False

    def nodeInCloselist(self, node):
        for nodetmp in self.closelist:
            if nodetmp.point.x == node.point.x \
            and nodetmp.point.y == node.point.y:
                return  True
        return False 

    def endNodeInOpenlist(self):
        for nodetmp in self.openlist:
            if nodetmp.point.x == self.endNode.point.x \
            and nodetmp.point.y == self.endNode.point.y:  
                return True  
        return False

    def getNodeFromOpenlist(self, node):
        for nodetmp in self.openlist:
            if nodetmp.point.x == self.endNode.point.x \
            and nodetmp.point.y == self.endNode.point.y:  
                return nodetmp  
        return None

    def searchOneNode(self, node):
        # search the node 

        # ignore the obstacle
        if self.map.isPass(node.point) != True:
            return
        # ignore the node which is in the closelist
        if self.nodeInCloselist(node):
            return
        # calculate the G value
        if abs(node.point.x - self.currentNode.point.x) == 1 and abs(node.point.y - self.currentNode.point.y) == 1:  
            gTmp = 14  
        else:  
            gTmp = 10 

        # if node is not in openlist then add it to it 
        if self.nodeInOpenlist(node) == False:
            node.father = self.currentNode
            node.setG()
            #calculate h
            node.setH(self.endNode)
            self.openlist.append(node)
            
        # if node is alreay in openlist, determine whether G is smaller form currentNode
        # to "node", if G is smaller, then recalculate G and change the father node
        else:
            if self.currentNode.g + gTmp < node.g:
                node.father = self.currentNode
                node.g = node.setG()
        return
    
    def searchNear(self):
        # search the nearest 8 nodes
        # (x-1, y-1)(x-1, y)(x-1, y+1)
        # (x,   y-1)(x,   y)(x,   y+1)
        # (x+1, y-1)(x+1, y)(x+1, y+1)
        # 
        if self.map.isPass(Point(self.currentNode.point.x - 1, self.currentNode.point.y)) or \
            self.map.isPass(Point(self.currentNode.point.x, self.currentNode.point.y -1)):
            self.searchOneNode(Node(Point(self.currentNode.point.x - 1, self.currentNode.point.y - 1)))
        
        self.searchOneNode(Node(Point(self.currentNode.point.x - 1, self.currentNode.point.y)))

        if self.map.isPass(Point(self.currentNode.point.x - 1, self.currentNode.point.y)) or \
            self.map.isPass(Point(self.currentNode.point.x, self.currentNode.point.y + 1)):
            self.searchOneNode(Node(Point(self.currentNode.point.x - 1, self.currentNode.point.y + 1)))

        self.searchOneNode(Node(Point(self.currentNode.point.x, self.currentNode.point.y - 1)))
        self.searchOneNode(Node(Point(self.currentNode.point.x, self.currentNode.point.y + 1)))

        if self.map.isPass(Point(self.currentNode.point.x, self.currentNode.point.y - 1)) or \
            self.map.isPass(Point(self.currentNode.point.x + 1, self.currentNode.point.y)):
            self.searchOneNode(Node(Point(self.currentNode.point.x + 1, self.currentNode.point.y - 1)))
        
        self.searchOneNode(Node(Point(self.currentNode.point.x + 1, self.currentNode.point.y)))

        if self.map.isPass(Point(self.currentNode.point.x + 1, self.currentNode.point.y)) or \
            self.map.isPass(Point(self.currentNode.point.x, self.currentNode.point.y + 1)):
            self.searchOneNode(Node(Point(self.currentNode.point.x + 1, self.currentNode.point.y + 1)))
        return

    def start(self):
        #add the startnode to the openlist
        self.startNode.setH(self.endNode)
        self.startNode.g = 0
        self.openlist.append(self.startNode)

        while True:
            # find the min F in openlist
            # add it to closelist and delet it in openlist
            self.currentNode = self.getMinFNode()
            self.openlist.remove(self.currentNode)
            self.closelist.append(self.currentNode)

            self.searchNear()

            #check if it is over
            if self.endNodeInOpenlist():
                nodetmp = self.getNodeFromOpenlist(self.endNode)  ##...还是有必要的，终止条件的判断？这里要好好看看
                while True:
                    self.pathlist.append(nodetmp)
                    if nodetmp.father != None:
                        nodetmp = nodetmp.father
                    else:
                        return True
            elif len(self.openlist) == 0:
                return False
        return True

    def setMap(self):
        for node in self.pathlist:
            self.map.setMap(node.point)
        return