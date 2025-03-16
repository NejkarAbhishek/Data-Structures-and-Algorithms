# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        nums=[]
        def traverse(root):
            if not root:
                return -1
            traverse(root.left)
            nums.append(root.val)
            traverse(root.right)
        
        traverse(root)
        return nums[k-1]