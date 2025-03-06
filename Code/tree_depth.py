class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def get_tree_depth(root):
    if root is None:
        return 0
    else:
        left_depth = get_tree_depth(root.left)
        right_depth = get_tree_depth(root.right)
        return max(left_depth, right_depth) + 1

# 示例用法
if __name__ == "__main__":
    # 构建一个简单的二叉树
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("树的深度是:", get_tree_depth(root))