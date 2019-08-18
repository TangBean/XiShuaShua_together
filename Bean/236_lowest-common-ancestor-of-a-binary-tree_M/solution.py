# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    Runtime: 68 ms, faster than 56.88% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
    """
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.find_lowest_common_ancestor(root, p, q)

    def find_lowest_common_ancestor(self, root, p, q):
        if not root:
            return
        if root == p or root == q:
            return root

        left_branch = self.find_lowest_common_ancestor(root.left, p, q)
        right_branch = self.find_lowest_common_ancestor(root.right, p, q)
        if left_branch and right_branch:
            return root
        return left_branch if left_branch else right_branch
