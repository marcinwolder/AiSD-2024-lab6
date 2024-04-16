"""
Uzupełnij 2 funkcje poniżej oznaczone jako "TODO". 
Nie modyfikuj kodu, który już istnieje.
Można tworzyć własne funkcje pomocnicze.
Po zaimplementowaniu rozwiązania komendy `pass` powinny być usunięte.
"""

from typing import List, Optional


class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(node_values: List[str]):
    if (
        not node_values
        or len(node_values) == 0
        or node_values[0].strip() == ""
        or node_values[0] == "null"
    ):
        return None
    root = Node(int(node_values[0]))
    queue = [(root, 0)]
    while queue:
        current_node, idx = queue.pop()
        left_idx = idx * 2 + 1
        right_idx = idx * 2 + 2
        if left_idx < len(node_values):  # left child
            value = node_values[left_idx]
            if value != "null":
                current_node.left = Node(int(value))
                if left_idx <= len(node_values) // 2:  # is not a leaf
                    queue.append((current_node.left, left_idx))

        if right_idx < len(node_values):  # right child
            value = node_values[right_idx]
            if value != "null":
                current_node.right = Node(int(value))
                if right_idx <= len(node_values) // 2:  # is not a leaf
                    queue.append((current_node.right, right_idx))

    return root


def is_same_tree(p: Optional[Node], q: Optional[Node]) -> bool:
    # TODO Mając podane dwa korzenie p i q reprezentujące dwa drzewa binarne, 
    # sprawdź są identyczne.
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False

    if p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, p.right)


def is_subtree(root: Optional[Node], subRoot: Optional[Node]) -> bool:
    # TODO Mając podane dwa korzenie root i subRoot reprezentujące dwa drzewa binarne,
    # sprawdź czy subRoot jest poddrzewem drzewa root.
    # Podpowiedź: wykorzystaj metodę is_same_tree
    if is_same_tree(root, subRoot):
        return True

    if root is None:
        return False

    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)


# nie zmieniaj poniższego kodu
if __name__ == "__main__":
    trees = input().strip().split(";")
    node_values1 = trees[0].strip().split(" ")
    node_values2 = trees[1].strip().split(" ")
    root1 = create_binary_tree(node_values1)
    root2 = create_binary_tree(node_values2)
    print(is_subtree(root1, root2), is_same_tree(root1, root2))
