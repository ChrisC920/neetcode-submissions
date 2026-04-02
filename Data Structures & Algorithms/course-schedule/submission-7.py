class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course -> prereq
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            
            if not preMap[course]:
                return True
            
            visited.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True