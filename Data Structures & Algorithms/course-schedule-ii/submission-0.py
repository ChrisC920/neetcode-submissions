class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.res = []
        # course -> prereq
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            
            if not preMap[course]:
                self.res.append(course)
                return True
            
            visited.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            preMap[course] = []
            self.res.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return self.res