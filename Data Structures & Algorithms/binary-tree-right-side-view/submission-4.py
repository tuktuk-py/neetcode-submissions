# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        output = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            rightMost = None
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    rightMost = curr
                    queue.append(curr.left)
                    queue.append(curr.right)
            if rightMost:
                output.append(rightMost.val)
        return output
