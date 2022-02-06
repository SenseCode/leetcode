# You have a data structure of employee information, including the employee's 
# unique ID, importance value, and direct subordinates' IDs. 
# 
#  You are given an array of employees employees where: 
# 
#  
#  employees[i].id is the ID of the iᵗʰ employee. 
#  employees[i].importance is the importance value of the iᵗʰ employee. 
#  employees[i].subordinates is a list of the IDs of the direct subordinates of 
# the iᵗʰ employee. 
#  
# 
#  Given an integer id that represents an employee's ID, return the total 
# importance value of this employee and all their direct and indirect subordinates. 
# 
#  
#  Example 1: 
# 
#  
# Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
# Output: 11
# Explanation: Employee 1 has an importance value of 5 and has two direct 
# subordinates: employee 2 and employee 3.
# They both have an importance value of 3.
# Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.
#  
# 
#  Example 2: 
# 
#  
# Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
# Output: -3
# Explanation: Employee 5 has an importance value of -3 and has no direct 
# subordinates.
# Thus, the total importance value of employee 5 is -3.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= employees.length <= 2000 
#  1 <= employees[i].id <= 2000 
#  All employees[i].id are unique. 
#  -100 <= employees[i].importance <= 100 
#  One employee has at most one direct leader and may have several subordinates.
#  
#  The IDs in employees[i].subordinates are valid IDs. 
#  
#  Related Topics 深度优先搜索 广度优先搜索 哈希表 👍 252 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        mp={employee.id: employee for employee in employees}
        print("mp", mp)

        def dfs(id):
            employee=mp[id]
            total=employee.importance+sum(dfs(subid) for subid in employee.subordinates)
            print("total",total)
            return total

        return dfs(id)
# leetcode submit region end(Prohibit modification and deletion)
