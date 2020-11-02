# https://leetcode.com/problems/shuffle-string/
# Best: https://leetcode.com/problems/shuffle-string/discuss/755923/Used-Cyclic-Sort-with-O(1)-SPACE-and-O(N)-Time-complexity

# Sol 1
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['']*len(indices)
        for index, char in enumerate(s):
            res[indices[index]] = char
        return "".join(res)
# Sol 2
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        visited = [False]*len(indices)
        strList = list(s)
        for i in range(len(indices)):
            j = i
            t = strList[i]
            while not visited[j]:
                t1 = strList[indices[j]]
                strList[indices[j]] = t
                visited[j] = True
                j = indices[j]
                t = t1
        return "".join(strList)
        
# Sol 3
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        resultList = ['']*len(indices)
        result = ''
        for i in range(len(indices)):
            resultList[indices[i]] = s[i]
        for char in resultList:
            result+=char
        return result
