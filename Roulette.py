import random
import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ruleta Rusa")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fuentes
FONT = pygame.font.SysFont("comicsans", 30)

# Cargar sonidos
SHOT_SOUND = pygame.mixer.Sound("shot.wav")
CLICK_SOUND = pygame.mixer.Sound("click.wav")

# Clase Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Clase CircularLinkedList
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def play_russian_roulette(self):
        if not self.head:
            print("La lista está vacía.")
            return

        bullet_position = random.randint(1, 6)
        current = self.head
        for _ in range(bullet_position - 1):
            current = current.next

        return current

# Función para dibujar texto
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    WIN.blit(img, (x, y))

# Función para obtener los nombres de los jugadores
def get_player_names():
    players = []
    num_players = int(input("Ingrese el número de jugadores (mínimo 2): "))
    for i in range(num_players):
        name = input(f"Ingrese el nombre del jugador {i + 1}: ")
        players.append(name)
    return players

# Función principal del juego
def main():
    run = True
    players = get_player_names()
    current_player = 0
    rounds = 0
    stats = {player: 0 for player in players}
    russian_roulette = CircularLinkedList()

    for i in range(1, 7):
        if i == 3:
            russian_roulette.append('Bala')
        else:
            russian_roulette.append(i)

    while run:
        WIN.fill(BLACK)

        # Dibujar información del jugador actual
        draw_text(f"Ronda: {rounds + 1}", FONT, WHITE, 10, 10)
        draw_text(f"Jugador actual: {players[current_player]}", FONT, WHITE, 10, 40)

        # Dibujar botones
        draw_text("Presiona Espacio para disparar", FONT, WHITE, 10, HEIGHT - 60)
        draw_text("Presiona 'q' para salir", FONT, WHITE, 10, HEIGHT - 30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    CLICK_SOUND.play()
                    current_node = russian_roulette.play_russian_roulette()
                    if current_node.data == 'Bala':
                        SHOT_SOUND.play()
                        draw_text(f"{players[current_player]} ha perdido.", FONT, RED, WIDTH // 2 - 100, HEIGHT // 2)
                        pygame.display.update()
                        pygame.time.delay(2000)
                        players.pop(current_player)
                        if len(players) == 1:
                            draw_text(f"{players[0]} ha ganado!", FONT, GREEN, WIDTH // 2 - 100, HEIGHT // 2 + 30)
                            pygame.display.update()
                            pygame.time.delay(2000)
                            run = False
                            stats[players[0]] += 1
                        else:
                            current_player = (current_player + 1) % len(players)
                            rounds += 1
                    else:
                        current_player = (current_player + 1) % len(players)
                elif event.key == pygame.K_q:
                    run = False

        pygame.display.update()

    # Mostrar estadísticas
    print("Estadísticas:")
    for player, wins in stats.items():
        print(f"{player}: {wins} victorias")

    pygame.quit()

if __name__ == "__main__":
    main()