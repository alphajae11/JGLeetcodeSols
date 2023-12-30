class Solution:
    def countGoodNodes(self, root: TreeNode, maxi: int) -> int:
        if root == None:
            return 0
        else:
            if root.val >= maxi:
                return 1 + self.countGoodNodes(root.left, root.val) + self.countGoodNodes(root.right, root.val)
            else:
                return 0 + self.countGoodNodes(root.left, maxi) + self.countGoodNodes(root.right, maxi)
    def goodNodes(self, root: TreeNode) -> int:
        return self.countGoodNodes(root, -100000)