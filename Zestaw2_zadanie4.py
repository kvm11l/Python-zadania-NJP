# Zadanie 4
# Za pomocą namedtuple i innych poznanych kolekcji zaimplementuj algorytm tworzący drzewo binarne.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_binary_tree(elements):
    if not elements:
        return None

    # Tworzenie korzenia drzewa
    root = Node(elements[0])

    # Tworzenie pustej kolejki
    queue = [root]

    # Indeks do śledzenia aktualnego elementu w liście elements
    i = 1

    # Przechodzenie przez elementy w liście elements
    while i < len(elements):
        # Pobranie węzła z kolejki
        node = queue.pop(0)

        # Dodanie lewego dziecka, jak istnieje
        if elements[i] is not None:
            left_child = Node(elements[i])
            node.left = left_child
            queue.append(left_child)

        i += 1

        # Sprawdzenie, czy jest jeszcze jeden element w liście elements
        if i < len(elements):
            # Dodanie prawego dziecka, jak istnieje
            if elements[i] is not None:
                right_child = Node(elements[i])
                node.right = right_child
                queue.append(right_child)

        i += 1

    return root

def inorder_traversal(root):
    if root is None:
        return []

    result = []

    # Rekurencyjnie przechodzenie lewego poddrzewa
    if root.left:
        result.extend(inorder_traversal(root.left))

    # Dodanie wartości korzenia do wyniku
    result.append(root.value)

    # Rekurencyjnie przechodzenie prawego poddrzewa
    if root.right:
        result.extend(inorder_traversal(root.right))

    return result

# Przykładowe użycie
if __name__ == '__main__':
    elements = [1, 2, 3, 4, 5]
    tree = create_binary_tree(elements)

    # Przechodzenie drzewa binarnego
    traversal_result = inorder_traversal(tree)
    print("Drzewo binarne inorder:", traversal_result)