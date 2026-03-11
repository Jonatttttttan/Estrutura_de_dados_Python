from tree import BinaryTree, Node, BinarySearchTree
import random

random.seed(77)

def random_tree(size=42):
    values = random.sample(range(1, 1000), size)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def example_tree():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree


bst = example_tree()
bst.inorder_traversal()

print("\n----")
bst.level_order_traversal()

'''print("\n----")
items = [1, 3, 981, 510 ,1000]
for item in items:
    r = bst.search(item)
    if r is None:
        print(item, "não encontrado")
    else:
        print(r.root.data, "encontrado")'''

