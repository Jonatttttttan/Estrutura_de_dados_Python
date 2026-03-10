from EstruturaDeDados.node import Node



# inserir na pilha
# remover da pilha
# observar o topo da pilha
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem): # O(1)
        #insere um elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size += 1


    def pop(self): # O(1)        #remove o elemento do topo da pilha
        if self._size >0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node
        raise IndexError("The stack is empty")



    def peek(self): #O(1)
        #retorna o topo da pilha sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")





    def __len__(self): # Sobrecarga de operador O(1)
        # Retorna o tamanho da lista
        return self._size


    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer =pointer.next
        return r

    def __str__(self):
        return self.__repr__()




# Sobrecarga de operador

pilha = Stack()




pilha.push(3)
pilha.push(7)
pilha.push("python")
pilha.push(True)
pilha.push(1.2)

pilha.pop()
print(pilha)
print("Tamanho da pilha -", len(pilha))



