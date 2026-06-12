class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 0 = circular sandwiches 1= square sandwiches
        # all students stand in a queue to get the sandwiches, each student either prefers square or circular sandwiches
        # the total number of sandwhiches in the caf is equal to the number of students
        # the sandwiches are place in a stack, at each step and will continue until theres none of the students left in the queue that wants the top sandwhich
        # 1. if the student at the fron of the queu prefers the sandwich on the top of the stack, they will take it and leave the queue (dequeue with counter of the sandwhich -1)
        # 2. otherwise they will leave it and go to the queue's end. (dequeue then enqueue)
        # input students [int,int,int,...](type of sandwhich they prefer) and sandwhiches [int,int,int,..](type of sandwhich they prefer)
        # output = int, return the number of students that are unable to eat (len(students))
        # basic syntax 
        # Establish an empty queue
        # queue = deque()
        # Enqueue: Add elements to the end (right)
        # queue.append("Task 1")
        # queue.append("Task 2")
        # Dequeue: Remove elements from the front (left)
        # first_item = queue.popleft() 
        # step by step
        # 1. the loop needs to be looped through students list first when sandwiches list iteration stays the same
        # for i in range(len(sandwiches)):
        #     print(f"looping through sandwiches list {sandwiches[i]}")
        #     for j in range(len(students)):
        #         print(f"looping through students list {students[j]}")
        #         print(f"Students queue before the verification {students}")
        #         if sandwiches[i] != students[j]:
        #             # need to have the students to move back of the list
        #             # students[-1] = students[j] # this way the original index value stays the same so that's shouldnt be right
        #             # print(students)
        n = len(students) # total count of students
        q = deque(students) # establishing queue with students preferences
        for sand in sandwiches: # looping through the sandwhiches type
            cnt = 0 # initalizing the count of the iteration
            while cnt < n and q[0] != sand: # count of the iteration is smaller than the total count of students and first student's sandwhich perference
                cur = q.popleft() # declaring that cur is the perference that student has and pop it out of the queue
                q.append(cur) # queue appending the student's perference again to the back
                cnt += 1 # amount of students that got scanned already, incrementing the count
            if q[0] == sand: # this is time when the student preference is matched with the sandwhich inventory
                q.popleft() # we take that student off the queue
                n -= 1 # count of the length of students get decremented
            else:
                break
        return n








