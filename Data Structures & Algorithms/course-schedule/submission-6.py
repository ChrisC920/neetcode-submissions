class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses < len(prerequisites):
            return False
        
        # course -> prereq
        mapping = dict()
        for course, prereq in prerequisites:
            mapping[course] = prereq
        seen = set()
        def helper(course, start):
            print(f'{course} {start}')
            if course == start:
                return False
            seen.add(course)
            if course not in mapping:
                return True
            return helper(mapping[course], start)

        res = True
        for course, prereq in mapping.items():
            if course not in seen:
                res = res and helper(prereq, course)
        return res