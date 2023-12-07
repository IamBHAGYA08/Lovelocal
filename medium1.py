
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = TreeNode(2)
q = TreeNode(8)

lca = lowestCommonAncestor(root, p, q)
print(lca.val) 