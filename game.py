import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

# Initialisiert das Pygame-Framework.
pygame.init()

# Initialisiert eine Schriftart für die Anzeige des Scores 
font = pygame.font.Font('arial.ttf', 25)
# Alternativ kann eine System-Schriftart verwendet werden 
#font = pygame.font.SysFont('arial', 25)

# Definiert eine Enumeration(Aufzählung)  für die Richtungen 
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

# Definiert ein benanntes Tupel Point(Liste) für die Koordinaten 
Point = namedtuple('Point', 'x, y')

# Definition der RGB-Farben für das Spiel 
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

# Größe der Blöcke in Pixel 
BLOCK_SIZE = 20
# Geschwindigkeit des Spiels 
SPEED = 40

# Die Hauptklasse des Spiels SnakeGameAI 
class SnakeGameAI:

    # Konstruktor der Klasse
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # Initialisiert das Anzeigefenster
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        # Das Spiel zurückzusetzen
        self.reset()


    # Setzt das Spiel zurück 
    def reset(self):
        # Setzt die Start-Richtung auf rechts
        self.direction = Direction.RIGHT
        # Platzierung des Kopfes der Schlange in der Mitte des Spielfelds 
        self.head = Point(self.w/2, self.h/2)
        # Initialisierung der Schlange mit drei Gliedern
        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]

        # Setzt den Score auf 0 
        self.score = 0
        # Setzt das Essen auf 0 und platziert es dann zufällig 
        self.food = None
        self._place_food()
        # Initialisiert die Frame-Iteration
        self.frame_iteration = 0


    # Platziert das Essen zufällig auf dem Spielfeld 
    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = Point(x, y)
        # Überprüft ob das Essen auf der Schlange platziert wurde und platziert es erneut 
        if self.food in self.snake:
            self._place_food()


    # Führt einen Spielzug aus 
    def play_step(self, action):
        # Erstellt die Frame-Iteration
        self.frame_iteration += 1
        # Sammelt Benutzereingaben und beendet das Spiel falls Gameover 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # Führt den Spielzug aus
        self._move(action) # Aktualisiert den Kopf der Schlange
        self.snake.insert(0, self.head)
        
        # Überprüft ob das Spiel vorbei ist
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            reward = -30
            return reward, game_over, self.score

        # Platziert neues Essen oder bewegt die Schlange weiter 
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()
        
        # Aktualisiert die Benutzeroberfläche und die Tickrate
        self._update_ui()
        self.clock.tick(SPEED)
        # Gibt Spielstatus und Score zurück
        return reward, game_over, self.score


    # Überprüft ob eine Kollision vorliegt
    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # Überprüft ob der Punkt die Spielfeldgrenzen oder die Schlange berührt
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        if pt in self.snake[1:]:
            return True

        return False


    # Aktualisiert die Benutzeroberfläche
    def _update_ui(self):
        # Zeichnet die Schlange und das Essen 
        self.display.fill(BLACK)

        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        # Zeigt den Score an
        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()


    # Bewegt die Schlange entsprechend der übergebenen Aktion 
    def _move(self, action):
        # Die Richtungen werden im Uhrzeigersinn definiert

        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        # Bestimmt die neue Richtung basierend auf der Aktion
        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx] # no change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx] # right turn r -> d -> l -> u
        else: # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx] # left turn r -> u -> l -> d

        # Setzt die neue Richtung
        self.direction = new_dir

        # Bewegt den Kopf der Schlange entsprechend der Richtung 
        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        # Aktualisiert die Position des Kopfes 
        self.head = Point(x, y)