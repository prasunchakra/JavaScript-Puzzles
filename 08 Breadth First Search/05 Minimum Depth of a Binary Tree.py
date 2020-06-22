"""
Find the minimum depth of a binary tree.
The minimum depth is the number of nodes
along the shortest path from the root node
to the nearest leaf node.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    mindepth = 0
    queue = deque()
    queue.append(root)
    while queue:
        mindepth += 1
        nodecount = len(queue)
        for _ in range(nodecount):
            node = queue.popleft()
            if not node.left and not node.right:
                return mindepth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return mindepth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
