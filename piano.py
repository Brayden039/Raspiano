import pygame
import time

# Initialize pygame
pygame.init()

# Set up the mixer for playing sounds
pygame.mixer.init()

# Load sounds (replace these with your own sound files)
sound_1 = pygame.mixer.Sound("path/to/sound_1.wav")
sound_2 = pygame.mixer.Sound("path/to/sound_2.wav")

# Define the key-to-sound mapping
key_sound_mapping = {
    pygame.K_1: sound_1,
    pygame.K_2: sound_2,
    # Add more key mappings as needed
}

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Check if the pressed key has a sound mapping
            if event.key in key_sound_mapping:
                # Play the corresponding sound
                key_sound_mapping[event.key].play()

    time.sleep(0.01)

# Clean up pygame
pygame.quit()
