# Given a 1-indexed array of integers numbers that is already sorted in non-
# decreasing order, find two numbers such that they add up to a specific target 
# number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1
#  < index2 <= numbers.length. 
# 
#  Return the indices of the two numbers, index1 and index2, added by one as an 
# integer array [index1, index2] of length 2. 
# 
#  The tests are generated such that there is exactly one solution. You may not 
# use the same element twice. 
# 
#  Your solution must use only constant extra space. 
# 
#  
#  Example 1: 
# 
#  
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We 
# return [1, 2].
#  
# 
#  Example 2: 
# 
#  
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We 
# return [1, 3].
#  
# 
#  Example 3: 
# 
#  
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We 
# return [1, 2].
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= numbers.length <= 3 * 10⁴ 
#  -1000 <= numbers[i] <= 1000 
#  numbers is sorted in non-decreasing order. 
#  -1000 <= target <= 1000 
#  The tests are generated such that there is exactly one solution. 
#  
#  Related Topics 数组 双指针 二分查找 👍 709 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        '''
numbers = [2,7,11,15], target = 9
Output: [1,2]
'''
    #此法超时 O（n2）:

    #         length=len(numbers)
    #         for i in range(0, length-1):
    #             for j in range(i+1,length):
    #                 if numbers[i]+numbers[j]==target:
    #                     return [i+1,j+1]

    # 因为是排序好的array，所以使用这个方法复杂度也还是高。
    #         premap={}
    #         length=len(numbers)

    #         for i, v in enumerate(numbers):
    #             diff=target -v
    #             if diff in premap:
    #                 return [premap[diff]+1, i+1]
    #             else:
    #                 premap[v]=i

    #         return

        l=0
        r=len(numbers)-1
        while l<r:
            curr=numbers[l]+numbers[r]
            if curr <target:
                l=l+1
            elif curr>target:
                r=r-1

            else:
                return [l+1,r+1]

        return
# leetcode submit region end(Prohibit modification and deletion)
