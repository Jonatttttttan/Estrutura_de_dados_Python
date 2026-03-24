from EstruturaDeDados.Fila.queue import Queue

ROOT = "root"

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data = None, node = None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else: self.root = None

    # percurso de ordem simétrica (o correto é "inorder" em inglês)
    def simetric_transversal(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            print("(", end="")
            self.simetric_transversal(node.left)
        print(node, end ='')
        if node.right:
            self.simetric_transversal(node.right)
            print(")", end="")
    # subarvore da esquerda, da direita e raiz
    def postorder_transversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_transversal(node.left)
        if node.right:
            self.postorder_transversal(node.right)
        print(node.data)

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

    # Percorre subarvore a esquerda, raiz, subarvore da direita
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node)
        if node.right:
            self.inorder_traversal(node.right)
    # Percorre por level de nós da esquerda para a direita
    def level_order_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            #print(node.data, end=(" "))
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            print(node.data, end=" ")


# Complexidade O(h)
class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
            print("leu")
            print(self.root.data)
            print("leu2")
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)


    def search(self, value):
        return self._search(value, self.root)


    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.right:
            node = node.right
        return node.data


# remoção de árvore binária
    def remove(self, value, node=ROOT):
        if node == ROOT:
            node = self.root

        if node is None:
            return node

        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substitute = self.min(node.right)
                node.data = substitute
                node.right = self.remove(substitute, node.right)
        return node




    ''' def search(self, value, node=0):
        if node == 0:
            node = self.root
        if node is None or node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)'''







# Fim da classe
if __name__ == "__main__":
    '''tree = BinaryTree(7)
    tree.root.left = Node(18)
    tree.root.right = Node(14)

    print(tree.root)
    print(tree.root.right)
    print(tree.root.left)'''

    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node("+")
    n3 = Node("*")
    n4 = Node("b")
    n5 = Node("-")
    n6 = Node("/")
    n7 = Node("c")
    n8 = Node("d")
    n9 = Node("e")

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2
    tree.simetric_transversal()
    print("")