class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:  
            return 0
        
        # we'll start at the extremes (leafs)
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        # it is a leaf, so we will start the backtracking by "adding" this level to the total
        if root.left is None and root.right is None:
            return 1
        
        # if it has a child, get the length of it
        if root.left is None:
            return 1 + rightDepth
        if root.right is None:
            return 1 + leftDepth

        # if it has two children, get the min of their lengths
        return min(leftDepth, rightDepth) + 1  