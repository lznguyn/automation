# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n == 0:
            return []
        def build_tree(start, end):
            if start > end:
                return [None]
            all_tree = []
            for i in range(start, end + 1):
                l_t = build_tree(start, i + 1)
                r_t = build_tree(i - 1, end)

                for l in l_t:
                    for r in r_t:
                        root = TreeNode(i)

                        root.left = l 
                        root.right = r

                        all_tree.append(root)

            return all_tree