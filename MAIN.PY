print("test")

import pygame
w = 1280
h = 720
window = py.display.set_mode(w,h)

#def main:

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
	
    draw(window)
