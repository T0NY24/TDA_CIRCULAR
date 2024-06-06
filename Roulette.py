import pygame
import random
import time

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ruleta Rusa")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Fuente
FONT = pygame.font.SysFont('comicsans', 40)

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

# Función para dibujar los nombres de los jugadores en la pantalla
def draw_players(players, current=None):
    WIN.fill(WHITE)
    y = 100
    for player in players:
        color = RED if player == current else BLACK
        text = FONT.render(player, 1, color)
        text_rect = text.get_rect(center=(WIDTH//2, y))
        WIN.blit(text, text_rect)
        y += 50
    pygame.display.update()

# Función para obtener el número de jugadores
def get_player_count():
    player_count = 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                elif event.key == pygame.K_BACKSPACE:
                    if player_count > 0:
                        player_count //= 10
                else:
                    if event.unicode.isdigit() and player_count < 10:
                        player_count = player_count * 10 + int(event.unicode)

        WIN.fill(WHITE)
        draw_text("Enter number of players (Press ENTER to start):", FONT, BLACK, WIDTH//2, 50)
        draw_text(str(player_count), FONT, BLACK, WIDTH//2, HEIGHT//2)
        pygame.display.update()

    return player_count

# Función para obtener los nombres de los jugadores predeterminados
def get_default_player_names(count):
    return [f"Player{i}" for i in range(1, count + 1)]

# Función para dibujar texto centrado en la pantalla
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    WIN.blit(text_surface, text_rect)

# Función para jugar la ruleta rusa
def play_roulette(players):
    cll = CircularLinkedList()
    for name in players:
        cll.append(name)

    bullet_position = random.randint(1, len(players))
    current = cll.get_node(bullet_position - 1)

    while len(players) > 1:
        spin = random.randint(1, len(players))
        for _ in range(spin - 1):
            current = current.next

        draw_players(players, current.data)
        time.sleep(1)

        print(f"{current.data} is out!")
        players.remove(current.data)
        cll.remove_node(current)
        current = current.next

    draw_players(players, players[0])
    print(f"{players[0]} wins!")
    time.sleep(2)

# Función principal
def main():
    player_count = get_player_count()
    player_names = get_default_player_names(player_count)
    play_roulette(player_names)

if __name__ == "__main__":
    main()
