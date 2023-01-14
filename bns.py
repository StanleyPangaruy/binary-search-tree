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

def buildTree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.addChild(elements[i])

    return root

if __name__ == '__main__':
    nameLetters = ['S', 'T', 'A', 'N', 'L', 'E', 'Y', 'J', 'O', 'H', 'I', 'V', 'R', 'P', 'G', 'U']
    lettersTree = buildTree(nameLetters)
    print("Is there a letter T on my name?", lettersTree.search('T'))
    print("Is there a letter J on my name?", lettersTree.search('J'))
    print("Is there a letter Z on my name?", lettersTree.search('Z'))
    print(lettersTree.inOrderTraversal())
