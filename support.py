from tree import BinaryTree, Node, BinarySearchTree
import random

#             '+'

def postorder_example_tree():
    tree = BinaryTree()
    n1 = Node("I")
    n2 = Node("N")
    n3 = Node("S")
    n4 = Node("C")
    n5 = Node("R")
    n6 = Node("E")
    n7 = Node("V")
    n8 = Node("A")
    n9 = Node("5")
    n0 = Node("3")

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0
    return tree

if __name__ == "__main__":
    '''tree = postorder_example_tree()
    print("Percurso em pós ordem")
    tree.postorder_transversal()
    print("Altura: ", tree.height())'''

    random.seed(77)

    values = random.sample(range(1, 1000), 42)

    bst = BinarySearchTree()

    for v in values:

        bst.insert(v)


    bst.inorder_traversal()

    items = [1, 3, 981, 510, 1000]
    for item in items:
        r = bst.search(item)
        if r is None:
            print(item, "não encontrado")
        else:
            print(r.root.data, "encontrado")
