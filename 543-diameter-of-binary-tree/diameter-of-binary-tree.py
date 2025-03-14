class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        def depth(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.diameter