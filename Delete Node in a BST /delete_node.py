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

        if root.val == key:
            root = None

        elif key < root.val:
            self.deleteNode(root.left, key)

        else:
            self.deleteNode(root.right, key)

        return root
