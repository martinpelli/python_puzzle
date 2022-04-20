import copy

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Tree():
    def __init__(self, incomingPuzzle, incomingIndexZero, incomingLevel):
        self.rightTree = None
        self.leftTree = None
        self.topTree = None
        self.botTree = None
        self.puzzle = incomingPuzzle
        self.indexZero = incomingIndexZero
        self.topMove = None
        self.bottomMove = None
        self.leftMove = None
        self.rightMove = None
        self.level = incomingLevel
        self.updateIndexZero()
        self.checkMoves()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def movingPieces(self, nextLevel):

        if(self.topMove):
            self.updateIndexZero()
            currentIndex = self.indexZero
            currentIndex[0] = currentIndex[0]-1
            numCurrentIndex = self.puzzle[currentIndex[0]][currentIndex[1]]

            newPuzzle = copy.deepcopy(self.puzzle)
            newPuzzle[self.indexZero[0]+1][self.indexZero[1]] = numCurrentIndex
            newPuzzle[currentIndex[0]][currentIndex[1]] = 0

            self.topTree = Tree(newPuzzle,currentIndex, nextLevel)
        else:
            print("Cannot move upward")

        if(self.bottomMove):
            self.updateIndexZero()
            currentIndex = self.indexZero
            currentIndex[0] = currentIndex[0]+1
            numCurrentIndex = self.puzzle[currentIndex[0]][currentIndex[1]]

            newPuzzle = copy.deepcopy(self.puzzle)
            newPuzzle[self.indexZero[0]-1][self.indexZero[1]] = numCurrentIndex
            newPuzzle[currentIndex[0]][currentIndex[1]] = 0

            self.botTree = Tree(newPuzzle,currentIndex, nextLevel)
        else:
            print("Cannot move downward")

        if(self.rightMove):
            self.updateIndexZero()
            currentIndex = self.indexZero
            currentIndex[1] = currentIndex[1]+1
            numCurrentIndex = self.puzzle[currentIndex[0]][currentIndex[1]]

            newPuzzle = copy.deepcopy(self.puzzle)
            newPuzzle[self.indexZero[0]][self.indexZero[1]-1] = numCurrentIndex
            newPuzzle[currentIndex[0]][currentIndex[1]] = 0

            self.rightTree = Tree(newPuzzle,currentIndex, nextLevel)
        else:
            print("Cannot move rightside")

        if(self.leftMove):
            self.updateIndexZero()
            currentIndex = self.indexZero
            currentIndex[1] = currentIndex[1]-1
            numCurrentIndex = self.puzzle[currentIndex[0]][currentIndex[1]]

            newPuzzle = copy.deepcopy(self.puzzle)
            newPuzzle[self.indexZero[0]][self.indexZero[1]+1] = numCurrentIndex
            newPuzzle[currentIndex[0]][currentIndex[1]] = 0

            self.leftTree = Tree(newPuzzle,currentIndex, nextLevel)
        else:
            print("Cannot move leftside")
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def updateIndexZero(self):
        for i in range(4):
            for j in range(4):
                if self.puzzle[i][j] == 0:
                    self.indexZero[0] = i
                    self.indexZero[1] = j
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def checkSumIsEqualTo30(self):
        vertically = False
        horizontally = False
        diagonals = False

        if(self.puzzle[0][0] + self.puzzle[0][1] + self.puzzle[0][2] + self.puzzle[0][3]) == 30:
            if(self.puzzle[1][0] + self.puzzle[1][1] + self.puzzle[1][2] + self.puzzle[1][3]) == 30:
                if(self.puzzle[2][0] + self.puzzle[2][1] + self.puzzle[2][2] + self.puzzle[2][3]) == 30:
                    if(self.puzzle[3][0] + self.puzzle[3][1] + self.puzzle[3][2] + self.puzzle[3][3]) == 30:
                        horizontally = True
        
        if(self.puzzle[0][0] + self.puzzle[1][0] + self.puzzle[2][0] + self.puzzle[3][0]) == 30:
            if(self.puzzle[0][1] + self.puzzle[1][1] + self.puzzle[2][1] + self.puzzle[3][1]) == 30:
                if(self.puzzle[0][2] + self.puzzle[1][2] + self.puzzle[2][2] + self.puzzle[3][2]) == 30:
                    if(self.puzzle[0][3] + self.puzzle[1][3] + self.puzzle[2][3] + self.puzzle[3][3]) == 30:
                        vertically = True

        if(self.puzzle[0][0] + self.puzzle[1][1] + self.puzzle[2][2] + self.puzzle[3][3]) == 30:
            if(self.puzzle[0][3] + self.puzzle[1][2] + self.puzzle[2][1] + self.puzzle[3][0]) == 30:
                diagonals = True
            
        if(vertically) and (horizontally) and (diagonals):
            return True
        else:
            return False
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def checkMoves(self):
        index = self.indexZero
        if(index[0]-1) >= 0:
            self.topMove = True
        else:
            self.topMove = False
        if(index[0]+1) <= 3:
            self.bottomMove = True
        else:
            self.bottomMove = False
        if(index[1]-1) >= 0:
            self.leftMove = True
        else:
            self.leftMove = False
        if(index[1]+1) <= 3:
            self.rightMove = True
        else:
            self.rightMove = False
        return
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    
    def preOrder(self, currentTree):

        if(currentTree != None):
            if(currentTree.checkSumIsEqualTo30()):
                print("SOLUCIÓN: ")
                print(currentTree.puzzle)
                return
            if(currentTree.topTree != None):
                currentTree.preOrder(currentTree.topTree)
            if(currentTree.botTree != None):
                currentTree.preOrder(currentTree.botTree)
            if(currentTree.rightTree != None):
                currentTree.preOrder(currentTree.rightTree)
            if(currentTree.leftTree != None):
                currentTree.preOrder(currentTree.leftTree)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    
    def createTree(self):
        if(self.level <= 10):
            nextLevel = self.level + 1
            self.movingPieces(nextLevel)
            if(self.topTree != None):
                self.topTree.createTree()
            if(self.botTree != None):
                self.botTree.createTree()
            if(self.rightTree != None):
                self.rightTree.createTree()
            if(self.leftTree != None):
                self.leftTree.createTree()
        

root = Tree(
[[0,1,2,3],
[4,5,6,7],
[8,9,10,11],
[12,13,14,15]]
, [0,0],0)

root.createTree()
root.preOrder(root)
