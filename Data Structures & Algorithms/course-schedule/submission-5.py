class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        indegree = [0] * numCourses
        q = collections.deque()

        taken = 0

        for course, prereq in prerequisites:
            preMap[prereq].append(course)
            indegree[course] += 1
        
        for i, n in enumerate(indegree):
            if n == 0:
                q.append(i)

        while q:
            course = q.popleft()
            for c in preMap[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
            taken += 1
        
        return taken == numCourses