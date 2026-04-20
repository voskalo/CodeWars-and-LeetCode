'''delete Node in a BST'''


# Definition for a binary tree node.
class TreeNode:
    '''smth'''
    def __init__(self, val=0, left=None, right=None):
        '''init'''
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''solution'''

    def deleteNode(self, root, key):
        '''main funct'''

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                return root.right

            elif not root.right:
                return root.left

            successor = self.findMin(root.right)
            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val)

        return root

    def findMin(self, node):
        current = node
        while current.left:
            current = current.left
        return current
