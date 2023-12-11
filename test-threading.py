import time
import threading
import pygame

def playSound(pygame_sound, channel):
	channel.play(pygame_sound)

# Initialize pygame
pygame.init()

pygame.mixer.init()

# Initialize Sounds
sound_1 = pygame.mixer.Sound("mixkit-atm-cash-machine-key-press-2841.wav")
sound_2 = pygame.mixer.Sound("mixkit-atm-cash-machine-key-press-2841.wav")

threads = []
for i in range(2):
	threads.append(threading.Thread())
