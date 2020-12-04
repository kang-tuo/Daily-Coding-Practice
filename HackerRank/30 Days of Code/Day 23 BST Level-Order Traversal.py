import sys


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

    def levelOrder(self, root):
        # Write your code here
        if root is not None:
            queue = [root]
            for node in queue:
                print(node.data, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


T = [3, 5, 4, 7, 2, 1]
myTree = Solution()
root = None
for i in range(len(T)):
    data = T[i]
    root = myTree.insert(root, data)
myTree.levelOrder(root)
