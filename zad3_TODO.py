"""
Uzupełnij 2 funkcje poniżej oznaczone jako "TODO". 
Nie modyfikuj kodu, który już istnieje.
Można tworzyć własne funkcje pomocnicze.
Po zaimplementowaniu rozwiązania komendy `pass` powinny być usunięte.
"""

from typing import List, Optional
import math


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


def get_height(root: Optional[Node]) -> int:
    # TODO: Mając dany korzeń drzewa binarnego root zwróć jego wysokość
    if root is None:
        return -1

    return max(get_height(root.left), get_height(root.right))+1


def is_balanced(root: Optional[Node]) -> bool:
    # TODO: Mając dany korzeń drzewa binarnego root sprawdź czy to drzewo jest zbalansowane.
    max_height = get_height(root)  # O(n)
    if get_height_diff(root, max_height) > max_height:  # O(n)
        return False
    return True


def get_height_diff(root: Optional[Node], max_height: int) -> int:
    # returns tree height or `max_height+1` if height diff between left/right subtree is >= 2
    # Warning! max_height has to be greater/equal actual tree height
    if root is None:
        return -1

    left_height = get_height_diff(root.left, max_height)
    right_height = get_height_diff(root.right, max_height)

    if abs(left_height-right_height) > 1:
        return max_height+1

    return max(left_height, right_height)+1

# nie modyfikuj poniższego kodu
if __name__ == "__main__":
    node_values = input().strip().split(" ")
    root = create_binary_tree(node_values)
    height = get_height(root)
    if_balanced = int(is_balanced(root))
    print(height, if_balanced)
