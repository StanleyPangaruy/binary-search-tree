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

        # traverse left tree
        if self.left:
            elements += self.left.inOrderTraversal()

        #traverse base node
        elements.append(self.data)

        #traverse right tree
        if self.right:
            elements += self.right.inOrderTraversal()

        return elements

def buildTree(elements):
    root = BinarySearchTreeNode(elements[8])

    for i in range(1,len(elements)):
        root.addChild(elements[i])

    return root

if __name__ == '__main__':
    numbers = [19, 20, 1, 14, 12, 5, 25, 10, 15, 8, 9, 22, 18, 16, 7, 21]
    numbersTree = buildTree(numbers)
    print(numbersTree.inOrderTraversal())