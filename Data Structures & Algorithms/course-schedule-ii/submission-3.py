class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)

        indegree = [0] * numCourses
        q = collections.deque()
        taken = []

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
            taken.append(prereq)
        
        return taken if len(taken) == numCourses else []