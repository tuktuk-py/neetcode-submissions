# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        bfs = deque()
        if root:
            bfs.append(root)
        while len(bfs)>0:
            level = []
            for i in range(len(bfs)):
                curr = bfs.popleft()
                level.append(curr.val)
                if curr.left:
                    bfs.append(curr.left)
                if curr.right:
                    bfs.append(curr.right)
            output.append(level)
        return output