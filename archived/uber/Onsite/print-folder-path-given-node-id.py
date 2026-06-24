from typing import List, Optional
class Solution:
    def findFolderPath(self, idList: List[int], children: List[List[int]], nameList: List[str], targetId: int) -> str:
        res = []
        name_map = {} # id -> name
        parent_map = {}
    
        for id, childrens, name in zip(idList, children, nameList):
            name_map[id] = name
            if len(childrens) > 0:
                for child in childrens:
                    parent_map[child] = id
        
        curr = targetId
        while curr in name_map:
            res.append(name_map[curr])
            if curr in parent_map:
                curr = parent_map[curr]
            else:
                break
        res.reverse()
        return ",".join(res)
    
        

s = Solution()
print(s.findFolderPath(
    idList=[0,3,8,9,7,5], 
    children=[[7,3,8],[],[9],[],[],[]],
    nameList=["rootA","docs3","media8","photo9","tmp7","archive5"],
    targetId=9))
