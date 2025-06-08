class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, value):
        self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    def print_tree(self):
        self._print_tree(self.root, "", "Root")

    def print_node_value(self, node, prefix, side):
        print(f"{prefix}{side}-> {node.value}")

    def _print_tree(self, node, prefix, side):
        if node is None:
            return

        self.print_node_value(node, prefix, side)
        prefix += "| "
        if node.left:
            self._print_tree(node.left, prefix, "L")
        if node.right:
            self._print_tree(node.right, prefix, "R")


# Ejemplo de uso:
if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(12)
    tree.insert(18)
    tree.insert(1)
    tree.insert(4)
    tree.print_tree()
