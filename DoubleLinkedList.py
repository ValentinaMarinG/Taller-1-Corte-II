from cmath import sqrt
from hashlib import new
from lib2to3.pytree import Node
from os import remove


class doubleLinkedList:
    #Creamos la clase nodo anidada enn la clase doubleLinkedList
    class Node:
        #Creamos el método inicializador de la clase nodo 
        def __init__(self,value):
            self.value = value
            self.next_node = None
            self.previous_node = None
            
    #Creamos el método inicializador de la clase doubleLinkedList
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    #Método para imprimir la lista doblemente enlazada
    def show_double_linked_list(self):
        #Lista que almacenara los nodos de la lista doblemente enlazada
        array_double_linked_list = []
        current_node = self.head
        while (current_node != None):
            #unicamente almacenamos en la lista el valor del nodo
            array_double_linked_list.append(current_node.value)
            current_node = current_node.next_node
        print(array_double_linked_list)
        
    #Método para añadir nodos al inicio de la lista
    def prepend_node(self,value):
        #Al nuevo nodo le asiganamos la estructura real de la clase Node 
        new_node = self.Node(value)
        #Validamos si no hay cabeza ni cola en la lista
        if self.head == None and self.tail == None:
            #La cabeza todo el valor del nuevo nodo
            self.head = new_node
            #La cola toma el valor de la cabeza
            self.tail = self.head
            self.length += 1
        else:
            #El enlace anterior de la actual cabeza conecta con el nuevo nodo
            self.head.previous_node = new_node
            new_node.next_node = self.head
            self.head = new_node
        self.length += 1
    
    #Método para añadir nodo al final de la lista, en la cola     
    def append_node(self,value):
        #Al nuevo nodo le asiganamos la estructura real de la clase Node 
        new_node = self.Node(value)
        #Validamos si no hay cabeza ni cola en la lista
        if self.head == None and self.tail == None:
            #La cabeza todo el valor del nuevo nodo
            self.head = new_node
            #La cola toma el valor de la cabeza
            self.tail = self.head
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node
        self.length += 1
            
    #Método para eliminar la cabeza de la lista
    def delete_head(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        elif self.head != None:
            #El nodo a eliminar es la cabeza
            remove_node = self.head
            #La nueva cabeza sera el nodo siguiente a la anterior cabeza
            self.head = remove_node.next_node
            remove_node.next_node = None
            self.head.previous_node = None
            print(f'Nodo eliminado: {remove_node.value}')
        self.length -= 1
    
    #Método para eliminar la cola de la lista       
    def pop_tail(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        elif self.head != None:
            #El nodo a eliminar es la cabeza
            remove_node = self.tail
            #La nueva cabeza sera el nodo siguiente a la anterior cabeza
            self.tail = remove_node.previous_node
            self.tail.next_node = None
            self.tail.previous_node = None
            print(f'Nodo eliminado: {remove_node.value}')
        self.length -= 1
            
    #Método para obtener nodo en un indice especifico
    def get(self,index):
        if index == self.length-1:
            return self.tail
        elif index == 0:
            return self.head
        elif  not (index >= self.length or index < 0):
            middle_index = int(self.length/2)
            contador = 0
            if index <= middle_index:
                current_node = self.head
                while(contador != index):
                    current_node = current_node.next_node
                    contador += 1
            else :
                contador =self.length-1
                current_node = self.tail
                while(contador != index):
                    current_node = current_node.previous_node
                    contador -= 1
            return current_node
        else :
            return None
        
    #Método para insertar un nodo en una posición especifica
    def insert(self,index,value):
        if index == self.length:
            return self.append_node(value)
        elif index == 1:
            return self.prepend_node(value)
        elif not (index >= self.length or index < 0):
            new_node = self.Node(value)
            nodos_anteriores = self.get(index-2)
            nodos_siguientes = nodos_anteriores.next_node
            nodos_anteriores.next_node = new_node
            new_node.previous_node = nodos_anteriores
            new_node.next_node = nodos_siguientes
            nodos_siguientes.previous_node = new_node
            self.length += 1
        else:
            return None  
        
    #Función para invertir la lista
    def reverse_list(self):
        nodeAux = None
        nodeAux2 = None
        current_node = self.head
        if self.length == 0:
                self.head = self.tail
                self.tail = self.head
        else:
            while(current_node != None):
                nodeAux2 = current_node.next_node
                current_node.next_node = nodeAux
                nodeAux = current_node
                current_node.previous_node = nodeAux2
                current_node = nodeAux2
            self.head = nodeAux
        
    #TALLER 1 - CORTE II

    #Método para actualizar el valor de un nodo especifico dado su indice con el cuadrado del nodo siguiente
    def update(self,index):
        #Cambia el value de un nodo dado un index
        if index >= 0 and index <= self.length:
            nodo_objetivo = self.get(index)
        if nodo_objetivo != None and nodo_objetivo.previous_node != None:
            try:
                nodo_objetivo.value = int(nodo_objetivo.previous_node.value)**2
            except ValueError:
                print(">>Nodo anterior es un str<<")
        else:
            print("No hay nodo anterior para actualizar el nodo")
            return None
         
    #Método para insertar un nuevo nodo si su valor es multiplo del nodo siguiente de donde se quiere insertar
    def insert_cuadrado_del_next_node(self,index,value):
        nodo_quesigue = self.get(index)
        if type(value) == int and type(nodo_quesigue) == int:
            if index == self.length:
                return self.append_node(value)
            elif index == 1:
                nodo_siguiente = self.get(index)
                if value%nodo_siguiente.value == 0:
                    return self.prepend_node(value)
            elif not (index >= self.length or index < 0):
                new_node = self.Node(value)
                nodos_anteriores = self.get(index-2)
                nodos_siguientes = nodos_anteriores.next_node
                if (new_node.value % nodos_siguientes.value) == 0:
                    nodos_anteriores.next_node = new_node
                    new_node.previous_node = nodos_anteriores
                    new_node.next_node = nodos_siguientes
                    nodos_siguientes.previous_nodo = new_node
                    self.length += 1
            else:
                return None
        else:
            if index == self.length:
                return self.append_node(value)
            elif index == 1:
                return self.prepend_node(value)
            elif not (index >= self.length or index < 0):
                new_node = self.Node(value)
                nodos_anteriores = self.get(index-2)
                nodos_siguientes = nodos_anteriores.next_node
                nodos_anteriores.next_node = new_node
                new_node.previous_node = nodos_anteriores
                new_node.next_node = nodos_siguientes
                nodos_siguientes.previous_node = new_node
                self.length += 1
            else:
                return None
            
    #Método que elimina un nodo de la lista dado un indice
    def delete_node(self,index):
        if index == 1:
            return self.delete_head()
        elif index == self.length:
            return self.pop_tail()
        elif index < self.length  or index <= 0:
            nodos_anteriores = self.get(index-2)
            nodo_removido = nodos_anteriores.next_node
            nodo_removido.next_node.previous_node = nodos_anteriores
            nodos_anteriores.next_node = nodo_removido.next_node
            self.length -= 1
        else:
            return None
            
    #Método que invierte la lista y cambia los valores de los nodos por la raiz cuadrada de los mismos
    def reverse_list_sqrt(self):
        self.raiz_cuadrada()
        nodeAux = None
        nodeAux2 = None
        current_node = self.head
        if self.length == 0:
                self.head = self.tail
                self.tail = self.head
        else:
            while(current_node != None):
                nodeAux2 = current_node.next_node
                current_node.next_node = nodeAux
                nodeAux = current_node
                current_node.previous_node = nodeAux2
                current_node = nodeAux2
            self.head = nodeAux
      
    #Método que convierte el valor de los nodos en su raíz cuadrada
    def raiz_cuadrada(self):
        current_node = self.head
        while (current_node != None):
            if type(current_node.value) == int:
                current_node.value  = sqrt(current_node.value)
            current_node = current_node.next_node