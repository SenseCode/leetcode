# Given a list of accounts where each element accounts[i] is a list of strings, 
# where the first element accounts[i][0] is a name, and the rest of the elements 
# are emails representing emails of the account. 
# 
#  Now, we would like to merge these accounts. Two accounts definitely belong 
# to the same person if there is some common email to both accounts. Note that even 
# if two accounts have the same name, they may belong to different people as 
# people could have the same name. A person can have any number of accounts initially, 
# but all of their accounts definitely have the same name. 
# 
#  After merging the accounts, return the accounts in the following format: the 
# first element of each account is the name, and the rest of the elements are 
# emails in sorted order. The accounts themselves can be returned in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],[
# "John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John",
# "johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.
# com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email 
# "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses 
# are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 
# 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] 
# would still be accepted.
#  
# 
#  Example 2: 
# 
#  
# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin",
# "Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co",
# "Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@
# m.co","Fern1@m.co","Fern0@m.co"]]
# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.
# co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.
# co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co",
# "Fern1@m.co","Fern5@m.co"]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= accounts.length <= 1000 
#  2 <= accounts[i].length <= 10 
#  1 <= accounts[i][j] <= 30 
#  accounts[i][0] consists of English letters. 
#  accounts[i][j] (for j > 0) is a valid email. 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 字符串 👍 343 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

    #     graph=collections.defaultdict(list)
    #     for account in accounts:
    #         master=account[1]
    #         for email in set(account[2:])
    #             graph[master].append(email)
    #             graph[email].append(master)
    #     print("graph",graph)
    #
    #     res=[]
    #     visited=set()
    #
    #     for account in accounts:
    #         emails=[]
    #         self.dfs(account[1],graph,visited,emails)
    #         if emails:
    #             res.append([account[0]]+sorted(emails))
    #     return res
    #
    # def dfs(self, email, graph, visited, emails):
    #     if email in visited:
    #         return
    #     visited.add(email)
    #     emails.append(email)
    #     for neighbor in graph[email]:
    #         self.dfs(neighbor,graph, visited, emails)

        graph=collections.defaultdict(set)
        emailToName={}

        for acct in accounts:
            name=acct[0]
            print('name',name)
            #build edge for all emails:
            email1=acct[1]
            emailToName[email1]=name
            print("1",emailToName)
            for email2 in acct[2:]:
                graph[email1].add(email2)
                graph[email2].add(email1)
                emailToName[email2]=name
                print("2",emailToName )
        ans=[]
        seen=set()
        print('emailToName',emailToName)
        print('graph',graph)

        for email in emailToName:
            if email not in seen:
                stack=[email]
                seen.add(email)
                emails=[]

                while stack:
                    cur=stack.pop()
                    emails.append(cur)

                    for nei in graph[cur]:
                        if nei not in seen:
                            stack.append(nei)
                            seen.add(nei)
                ans.append([emailToName[email]]+sorted(emails))

        return ans

# leetcode submit region end(Prohibit modification and deletion)
