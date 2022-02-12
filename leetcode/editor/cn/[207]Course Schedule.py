# There are a total of numCourses courses you have to take, labeled from 0 to 
# numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai,
#  bi] indicates that you must take course bi first if you want to take course ai.
#  
# 
#  
#  For example, the pair [0, 1], indicates that to take course 0 you have to 
# first take course 1. 
#  
# 
#  Return true if you can finish all courses. Otherwise, return false. 
# 
#  
#  Example 1: 
# 
#  
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
#  
# 
#  Example 2: 
# 
#  
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you 
# should also have finished course 1. So it is impossible.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= numCourses <= 10⁵ 
#  0 <= prerequisites.length <= 5000 
#  prerequisites[i].length == 2 
#  0 <= ai, bi < numCourses 
#  All the pairs prerequisites[i] are unique. 
#  
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 👍 1113 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
    #set graph with linked list:
        preMap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        print("preMap", preMap)

    #set visited list:
        visit_set=set()

        def dfs(crs):
            if crs in visit_set:# course be visited, then it's a loop, return False
                return False
            if preMap[crs]==[]:#pre 选修课不存在,说明可以选课
                return True
            visit_set.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit_set.remove(crs)
            preMap[crs]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False

        return True





# leetcode submit region end(Prohibit modification and deletion)
