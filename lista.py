from node import Node


class Lista:
    inicio = None

    def _init_(self):
        self.inicio = None

    def adicionar(self, valor):
        if (self.inicio == None):
            self.inicio = Node(valor, None)
        else:
            aux = self.inicio
            while (aux.proximo != None):
                aux = aux.proximo

            aux.proximo = Node(valor, None)

    def show(self):
        aux = self.inicio
        print("[", end='')

        while (aux != None):
            print(f"{aux.valor}, ", end='')
            aux = aux.proximo
            
        print("]")

    def remo_one(self, valor):
        aux = self.inicio    

        if aux == None:         
          return

        if aux != None:
          if aux.valor == valor:
            self.inicio = self.proximo
            self = None                    

        while aux != None:         
          if aux.valor == valor:           
            break
          prev = aux
          aux = aux.proximo
        prev.proximo = aux.proximo
        aux = None

    def remo_all(self,valor):
        aux = self.inicio

        while aux != None:
          self.remo_one(valor)
          aux = aux.proximo