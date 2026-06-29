class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses < len(prerequisites):
            return False
        
        # course -> prereq
        mapping = dict()
        for course, prereq in prerequisites:
            if course == prereq:
                return False
            mapping[course] = prereq
        
        self.count = numCourses
        seen = set()
        def helper(course):
            if course in seen or course not in mapping:
                return
            self.count -= 1
            seen.add(course)
            helper(mapping[course])

        for course, prereq in mapping.items():
            if course not in seen:
                helper(course)
        print(self.count)
        return True if self.count > 0 else False