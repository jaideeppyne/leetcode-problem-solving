class Solution:
	def inorder(self, root, v):
		if root == None:
			return None
		self.inorder(root.left, v)
		v.append(root.val)
		self.inorder(root.right, v)

	def kthSmallest(self, root: TreeNode, k: int) -> int:
		v = []
		self.inorder(root, v)
		return v[k-1]
