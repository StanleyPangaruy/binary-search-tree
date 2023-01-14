# Create a demo using the letters in your fullname as the content of the binary tree.
# Upload all source code in new github repository.
# Create a demo then send to my messenger
# Deadline is today Jan14 4pm

#create a class for binary search tree code
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            # adds data in the left subtree
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # adds data in the right subtree
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def inOrderTraversal(self):
        elements = []

        #recur left tree
        if self.left:
            elements += self.left.inOrderTraversal()

        #recur base node
        elements.append(self.data)

        #recur right tree
        if self.right:
            elements += self.right.inOrderTraversal()

        return elements


    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def findMin(self):
        if  self.left is None:
            return self.data
        return self.left.findMin()

    def findMax(self):
        if  self.right is None:
            return self.data
        return self.right.findMax()

    def calculateSum(self):
        leftSum = self.left.calculateSum() if self.left else 0
        rightSum = self.right.calculateSum() if self.right else 0
        return self.data + leftSum + rightSum

def buildTree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.addChild(elements[i])

    return root

if __name__ == '__main__':
    nameLetters = ['S', 'T', 'A', 'N', 'L', 'E', 'Y', 'J', 'O', 'H', 'I', 'V', 'R', 'P', 'G', 'U']
    numbers = [19, 29, 1, 14, 12, 5, 25, 10, 15, 8, 9, 22, 18, 16, 7, 21,]
    lettersTree = buildTree(nameLetters)
    numbersTree = buildTree(numbers)
    print("Is there a letter T on my name?", lettersTree.search('T'))
    print("Is there a letter Z on my name?", lettersTree.search('Z'))
    print('In order traversal gives this sorted list: ' ,lettersTree.inOrderTraversal())
    print('Min: ',lettersTree.findMin())
    print('Max: ',lettersTree.findMax())
    print('Sum: ', numbersTree.calculateSum())