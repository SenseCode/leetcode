# Given the root of a binary tree, return its maximum depth. 
# 
#  A binary tree's maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,null,2]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁴]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1095 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
     root-->3
   depth--->(0, 20)+1
   20-->(15,7)+1
   15-->(3, none)+1
        """
        depth=0
        if not root:
            return 0
        depth+=1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) +1

# leetcode submit region end(Prohibit modification and deletion)
