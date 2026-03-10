from EstruturaDeDados.node import Node



# inserir na pilha
# remover da pilha
# observar o topo da pilha
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0


    def push(self, elem): # O(1)
        #insere um elemento na pilha
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if self.first is None:
            self.first = node

        self._size +=1



    def pop(self): # O(1)        #remove o elemento do topo da pilha
        if self.first is not None:
            elem = self.first.data
            self.first = self.first.next
            self._size -= 1
            return elem
        raise IndexError("The queue is empty")


    def peek(self): #O(1)
        #retorna o topo da pilha sem remover
        if self.first is not None:
            elem = self.first.data
            return elem
        raise IndexError("The queue is empty")





    def __len__(self): # Sobrecarga de operador O(1)
        # Retorna o tamanho da lista
        return self._size



    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while (pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        else:
            return "Empty queue"

    def __str__(self):
        return self.__repr__()




# Sobrecarga de operador

fila = Queue()




fila.push(3)
fila.push(7)
fila.push("python")
fila.push(True)
fila.push(1.2)

fila.pop()
print(fila)
print("Tamanho da pilha -", len(fila))



