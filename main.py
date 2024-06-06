class Nodo:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None
    
    def agregar_estudiante(self, estudiante):
        nuevo_nodo = Nodo(estudiante)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo
        print(f"Estudiante {estudiante} agregado.")
    
    def eliminar_estudiante(self):
        if self.cima is None:
            print("La pila está vacía. No hay estudiantes para eliminar.")
        else:
            estudiante_eliminado = self.cima.estudiante
            self.cima = self.cima.siguiente
            print(f"Estudiante {estudiante_eliminado} eliminado.")
    
    def mostrar_pila(self):
        actual = self.cima
        print("Estudiantes en la pila:")
        while actual:
            print(actual.estudiante)
            actual = actual.siguiente


pila_estudiantes = Pila()

pila_estudiantes.agregar_estudiante("Juan Pérez")
pila_estudiantes.agregar_estudiante("Ana García")
pila_estudiantes.agregar_estudiante("Luis Gómez")

pila_estudiantes.mostrar_pila()

pila_estudiantes.eliminar_estudiante()
pila_estudiantes.mostrar_pila()

pila_estudiantes.eliminar_estudiante()
pila_estudiantes.eliminar_estudiante()
pila_estudiantes.eliminar_estudiante()  # Intento de eliminar cuando la pila está vacía

pila_estudiantes.mostrar_pila()
