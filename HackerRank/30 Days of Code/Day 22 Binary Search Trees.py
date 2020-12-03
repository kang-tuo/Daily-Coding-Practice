class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        # Write your code here
        if root.left is None and root.right is None:
            return 0

        height_left = height_right = 0
        if root.left is not None:
            height_left = self.getHeight(root.left)
        if root.right is not None:
            height_right = self.getHeight(root.right)

        height = max(height_left, height_right)

        return height + 1


# T = [20, 50, 35, 44, 9, 15, 62, 11, 13]
T = [3, 5, 2, 1, 4, 6, 7]

myTree = Solution()
root = None
for i in range(len(T)):
    data = T[i]
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
