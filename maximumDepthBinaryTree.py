# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepthHelper(self, node, depth):
        # recursive cases
        if (node.left and node.right):
            return max(self.maxDepthHelper(node.left, depth+1),
                       self.maxDepthHelper(node.right, depth+1))
        elif(node.left):
            return self.maxDepthHelper(node.left, depth+1)
        elif(node.right):
            return self.maxDepthHelper(node.right, depth+1)
        # base case, no children nodes
        else:
            return depth
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # check for empty tree
        if (not root):
            return 0
        else:
            return self.maxDepthHelper(root, 1)
