# Given a binary tree, determine if it is height-balanced. 
# 
#  For this problem, a height-balanced binary tree is defined as: 
# 
#  
#  a binary tree in which the left and right subtrees of every node differ in 
# height by no more than 1. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 5000]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
#  Related Topics 树 深度优先搜索 二叉树 👍 876 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self,root):
        if not root:
            return 0
        return max(self.height(root.left),self.height(root.right))+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        lh=self.height(root.left)
        rh=self.height(root.right)
        if abs(lh-rh)<=1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else: return False
# leetcode submit region end(Prohibit modification and deletion)



