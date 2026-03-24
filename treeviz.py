import graphviz
from EstruturaDeDados.test_tree import example_tree, random_tree

def preorder_traversal(tree, dot):
    # visita a raiz
    dot.node(str(tree.data), str(tree.data))
    if tree.left:
        preorder_traversal(tree.left, dot)
        dot.edge(str(tree.data), str(tree.left.data))
    if tree.right:
        preorder_traversal(tree.right, dot)
        dot.edge(str(tree.data), str(tree.right.data))


def make_viz(tree, name):
    dot = graphviz.Digraph(comment=name)
    preorder_traversal(tree.root, dot)
    dot.render(f'viz/{name}.gv', view=True).replace("\\", "/")

if __name__ =='__main__':
    tree= example_tree()
    random = random_tree()
    make_viz(random, "expressao_random")