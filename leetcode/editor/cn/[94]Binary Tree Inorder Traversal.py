# Given the root of a binary tree, return the inorder traversal of its nodes' 
# values. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# Follow up: Recursive solution is trivial, could you do it iteratively? 
# Related Topics 栈 树 深度优先搜索 二叉树 👍 1245 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        def helper(root):
            if root is None:
                return []
            helper(root.left)
            print("left",root.left)
            result.append(root.val)
            print("root",root.val)
            helper(root.right)
            print("right",root.right)
        helper(root)
        print("result", result)
        return result






# leetcode submit region end(Prohibit modification and deletion)
