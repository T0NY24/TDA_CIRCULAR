import random
import time

# Clase Nodo
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Clase Lista Enlazada Circular
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def get_node(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def remove_node(self, node):
        if self.head == node:
            self.head = self.head.next
        current = self.head
        while current.next != node:
            current = current.next
        current.next = node.next

# Función para jugar la ruleta rusa
def play_roulette(players):
    cll = CircularLinkedList()
    player_names = []

    for i in range(1, players + 1):
        name = input(f"Enter name for Player {i}: ")
        cll.append(name)
        player_names.append(name)

    print("Starting the game with players:", player_names)

    bullet_position = random.randint(1, players)
    current = cll.get_node(bullet_position - 1)
    print(f"The bullet is in position {bullet_position}")

    current = cll.head
    while players > 1:
        spin = random.randint(1, players)
        for _ in range(spin - 1):
            current = current.next

        print(f"{current.data} is out!")
        player_names.remove(current.data)
        cll.remove_node(current)
        current = current.next
        players -= 1

    print(f"{current.data} wins!")

# Jugar con 6 jugadores
play_roulette(6)
