def depth(node):
    if node is None:  
        return 0
    
    # we'll start at the extremes (leafs)
    leftDepth = depth(node.left)
    rightDepth = depth(node.right)

    # it is a leaf, so we will start the backtracking by "adding" this level to the total
    if node.left is None and node.right is None:
        return 1
    
    # if it has a child, get the length of it
    if node.left is None:
        return 1 + rightDepth
    if node.right is None:
        return 1 + leftDepth

    # if it has two children, get the min of their lengths
    return min(leftDepth, rightDepth) + 1
    
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return depth(root)         