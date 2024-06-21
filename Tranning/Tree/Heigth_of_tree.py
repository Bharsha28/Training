                                
# Node structure for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to check if a binary tree is balanced

    # Function to calculate the height of a subtree
    def getHeight(self, root):
        # Base case: if the current node is NULL,
        # return 0 (height of an empty tree)
        if not root:
            return 0
        
        # Recursively calculate the height
        # of left and right subtrees
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        # Return the maximum height of left and right subtrees
        # plus 1 (to account for the current node)
        return max(leftHeight, rightHeight) + 1

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

# Creating an instance of the Solution class
solution = Solution()
print(solution.getHeight(root)-1)
                                
                            