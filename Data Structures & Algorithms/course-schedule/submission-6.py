class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        indegree = [0] * numCourses
        q = collections.deque()
        taken = 0

        for course, prereq in prerequisites:
            preMap[prereq].append(course)
            indegree[course] += 1
        
        for course in range(len(indegree)):
            if indegree[course] == 0:
                q.append(course)
        
        while q:
            prereq = q.popleft()

            for course in preMap[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
            
            taken += 1

        return taken == numCourses