class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visited = set()

        # map prereqs onto preMap
        for prereq in prerequisites:
            preMap[prereq[0]].append(prereq[1])
        
        print(preMap)

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            preMap[crs] = []
            visited.remove(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

        