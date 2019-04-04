# Maximum path sum I
# Answer: 1074


class Node():
    def __init__(self, value, depth, left=None, right=None):
        self.value = value
        self.depth = depth
        self.left = left  # left neighbor node
        self.right = right  # right neighbor node


def parse_tree(file_content):
    tree = []  # array to hold the tree nodes
    # create all the nodes in the tree
    lines = file_content.split('\n')
    for depth, line in enumerate(lines):
        values = list(map(int, line.split()))
        for i, value in enumerate(values):
            node = Node(value, depth)
            tree.append(node)

    # populate left and right neighbors
    for i, node in enumerate(tree):
        if node.depth != (len(lines) - 1):
            left_index = i + node.depth + 1
            right_index = left_index + 1
            node.left = tree[left_index]
            node.right = tree[right_index]

    return tree


def maximum_path_sum(node):
    if node is None:
        return 0
    return node.value + max(maximum_path_sum(node.left), maximum_path_sum(node.right))


if __name__ == "__main__":
    file_name = input()
    with open(file_name) as f:
        file_content = f.read()
    tree = parse_tree(file_content)
    root = tree[0]
    print(maximum_path_sum(root))
