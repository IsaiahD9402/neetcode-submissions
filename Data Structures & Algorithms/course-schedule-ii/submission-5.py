class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        indegree = [0] * numCourses

        courseMap = defaultdict(list)

        for course, prereq in prerequisites:
            courseMap[prereq].append(course)
            indegree[course] += 1
        
        q = collections.deque()
        for c in range(len(indegree)):
            if indegree[c] == 0:
                q.append(c)
                res.append(c)
        
        taken = 0

        while q:
            course = q.popleft()

            for nxt in courseMap[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
                    res.append(nxt)

        return res if len(res) == numCourses else []