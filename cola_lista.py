from abc import ABC, abstractmethod

class Cola(ABC):
    @abstractmethod
    def encolar(self, elemento):
        pass

    @abstractmethod
    def desencolar(self):
        pass

    @abstractmethod
    def frente(self):
        pass

    @abstractmethod
    def esta_vacia(self):
        pass

    @abstractmethod
    def tamano(self):
        pass
    

# Clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Implementación concreta de la Cola usando lista enlazada
class ColaEnlazada(Cola):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._tamano = 0

    def encolar(self, elemento):
        nuevo_nodo = Nodo(elemento)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self._tamano += 1

    def desencolar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.cola = None
        self._tamano -= 1
        return dato

    def frente(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.cabeza.dato

    def esta_vacia(self):
        return self.cabeza is None

    def tamano(self):
        return self._tamano

# Ejemplo de uso en sistema de procesamiento de pedidos
class Pedido:
    def __init__(self, id_pedido, descripcion):
        self.id_pedido = id_pedido
        self.descripcion = descripcion

# Crear la cola de pedidos
cola_pedidos = ColaEnlazada()

# Encolar algunos pedidos
cola_pedidos.encolar(Pedido(1, "Pedido de cliente 1"))
cola_pedidos.encolar(Pedido(2, "Pedido de cliente 2"))
cola_pedidos.encolar(Pedido(3, "Pedido de cliente 3"))

# Procesar pedidos
while not cola_pedidos.esta_vacia():
    pedido = cola_pedidos.desencolar()
    print(f"Procesando: {pedido.descripcion}")

# Salida esperada:
# Procesando: Pedido de cliente 1
# Procesando: Pedido de cliente 2
# Procesando: Pedido de cliente 3
