# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkBST(self, root: Optional[TreeNode], mini: int, maxi: int) -> bool:
        if root == None:
            return True
        else:
            if root.val >= maxi or root.val <= mini:
                print(maxi)
                print(mini)
                print(root.val)
                return False
            else:
                return self.checkBST(root.left, mini, root.val) and self.checkBST(root.right, root.val, maxi)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root.left, -math.pow(2, 31) - 1, root.val) and self.checkBST(root.right, root.val,
                                                                                          math.pow(2, 31))