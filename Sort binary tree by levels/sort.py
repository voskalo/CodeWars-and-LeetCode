'''Sort binary tree by levels'''
from collections import deque

class Node:
    '''node cls'''
    def __init__(self, L, R, n):
        '''init'''
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node: 'Node'):
    '''main funct'''

    if not node:
        return []

    res = []
    dq = deque([node])
    while dq:
        cur = dq.popleft()
        res.append(cur.value)

        if cur.left:
            dq.append(cur.left)

        if cur.right:
            dq.append(cur.right)

    return res
