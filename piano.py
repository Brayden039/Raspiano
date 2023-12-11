import pygame
import time

# Initialize pygame
pygame.init()

# Set up the mixer for playing sounds
pygame.mixer.init()

# Load sounds (replace these with your own sound files)
sound_1 = pygame.mixer.Sound("mixkit-atm-cash-machine-key-press-2841.wav")
# Define the key-to-sound mapping
key_sound_mapping = {
    pygame.K_1: sound_1,
    #the key to the right of the _ is the one that needs pressed. _z to press z to play a sound
    # Add more key mappings as needed
}

display = pygame.display.set_mode((300, 300))

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
