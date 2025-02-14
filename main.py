# the game is still in development!

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500, 700
BG_COLOR = (255, 182, 193)
TEXT_COLOR = (50, 50, 50)
FONT = pygame.font.Font(None, 28)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("i love meow <3")

messages = [
    ["hi there! i've been waiting for you... "],
    ["You received a strange message..."]
]
choices = [
    [("wait a second... who is this?!"), ("oh... hey there!")],
    [("open it", "ignore it")]
]
current_choice = 0
chat_history = ["Welcome to the chat!"]

def draw_chat():
    screen.fill(BG_COLOR)
    y_offset = HEIGHT - 200

    for msg in chat_history[-10:]:
        text_surface = FONT.render(msg, True, TEXT_COLOR)
        screen.blit(text_surface, (20, y_offset))
        y_offset -= 40

    if current_choice < len(choices):
        pygame.draw.rect(screen, (255, 182, 193), (20, HEIGHT-80, WIDTH-40, 60), border_radius=10)
        choice1 = FONT.render(choices[current_choice][0], True, BLACK)
        choice2 = FONT.render(choices[current_choice][1], True, BLACK)
        screen.blit(choice1, (30, HEIGHT-70))
        screen.blit(choice2, (30, HEIGHT-40))

    pygame.display.flip()

running = True
while running:
    draw_chat()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 and current_choice < len(choices):
                chat_history.append(f"> {choices[current_choice][0][0]}")
                chat_history.append(messages[current_choice][0])
                current_choice += 1
                chat_history.append(f"> {choices[current_choice][0]}")
                chat_history.append(messages[current_choice])
                current_choice += 1
            elif event.key == pygame.K_2 and current_choice < len(choices):
                chat_history.append(f"> {choices[current_choice][0][1]}")
                chat_history.append(messages[current_choice][1])
                current_choice += 1
                chat_history.append(f"> {choices[current_choice][1]}")
                chat_history.append(messages[current_choice])
                current_choice += 1

pygame.quit()
sys.exit()
