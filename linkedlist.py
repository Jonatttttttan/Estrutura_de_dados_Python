from node import Node

# sequencial = []
# sequencial.append(7)


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem): #O(N)
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head
            while (pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size += 1

    def __len__(self): # Sobrecarga de operador O(1)
        # retorna o tamanho da lista
        return self._size

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def set(selfself, index, elem):
        # lista.set(5, 9)
        pass

    def __getitem__(self, index): #O(N)
        #a = lista[5]

        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, elem): #O(N)
        #a = lista[9]

        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem

        else:
            raise IndexError("list index out of range")

    def index(self, elem): #O(N)
        """Retorna o índice do elemento na lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i+=1
        raise ValueError("{} is not in list".format(elem))

# Inserir elemento em qualquer índice
    def insert(self, index, elem): #O(N)
        node = Node(elem)
        if index == 0:

            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size +=1

    def remove(self, elem): #O(N)
        if self.head == None:
            raise ValueError("list is empty")
        elif self.head.data == elem:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size -= 1
                    return True
                ancestor = pointer
                pointer = pointer.next

            raise ValueError("{} is not in list".format(elem))

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer =pointer.next
        return r

    def __str__(self):
        return self.__repr__()




# Sobrecarga de operador


lista = LinkedList()

lista.append(7)
lista.append(80)

print("Tamanho -", len(lista))

print("Índice 1 -", lista[1])

lista.__setitem__(1, 6)
print("Lista 1 - setItem -", lista[1])

print(lista.index(6))

print("Lista 0 - sem insert:", lista[0])
lista.insert(0, 71)
print("\n INSERT\n")
print("Lista 0 após insert -", lista[0])
print("Lista 1 -", lista[1])
lista.insert(1, 90)

print("\nREMOVE\n")
print(lista)
lista.remove(90)
print("Índice 0 após remove -", lista[0])
#lista.remove(90)

print(lista)


