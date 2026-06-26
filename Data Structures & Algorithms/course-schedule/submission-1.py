class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        prereqmap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereqmap[crs].append(pre)
        
        # for key,val in prereqmap.items():
        #     print(key, val)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if prereqmap[crs] == []:    # remember if prereqmap[crs] = [] eg: 4:[]
                return True
            
            
            visited.add(crs) # add to visit set since it did not reach end or not in visited
            
            for pre in prereqmap[crs]:
                if not dfs(pre):
                    return False
            
            # remove crs from visited set for next dfs
            # update premap[crs] = [] so 
            # whenever we come across crs again we can just

            visited.remove(crs)
            prereqmap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):return False
        
        return True

