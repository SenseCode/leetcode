# Given the root of a binary tree, determine if it is a complete binary tree. 
# 
#  In a complete binary tree, every level, except possibly the last, is 
# completely filled, and all nodes in the last level are as far left as possible. It can 
# have between 1 and 2ʰ nodes inclusive at the last level h. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values 
# {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as 
# possible.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 100]. 
#  1 <= Node.val <= 1000 
#  
#  Related Topics 树 广度优先搜索 二叉树 👍 172 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """


        queue=[root]
        see_gap=False
        while queue:
            node=queue.pop(0)
            print('node',node)
            if not node:
                see_gap=True
            else:
                if see_gap:
                    print('see gap', see_gap)
                    return False
                queue.append(node.left)
                print('left',queue)

            queue.append(node.right)
            print('right',queue)

        return True
# leetcode submit region end(Prohibit modification and deletion)
