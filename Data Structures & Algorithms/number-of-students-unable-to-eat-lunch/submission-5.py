class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student = Counter(students)
        ans = len(students)
        for i in sandwiches:
            if i in student and student[i]>0:
                student[i] -= 1
                ans -= 1
            else:
                return ans
        return ans