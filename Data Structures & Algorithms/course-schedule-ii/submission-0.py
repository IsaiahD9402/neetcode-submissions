class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        visited = set()

        visiting = set()

        output = []

        # map prereqs onto preMap
        for prereq in prerequisites:
            preMap[prereq[0]].append(prereq[1])
        
        print(preMap)

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visited.add(crs)
            visiting.remove(crs)
            output.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return output