import pygame
import time

# Initialize pygame
pygame.init()

# Set up the mixer for playing sounds
pygame.mixer.init()

# Load sounds (replace these with your own sound files)
sound_1 = pygame.mixer.Sound("mixkit-atm-cash-machine-key-press-2841.wav")
sound_2 = pygame.mixer.Sound("mixkit-atm-cash-machine-key-press-2841.wav")
# Add more sounds as needed
sound_3 = pygame.mixer.Sound("mixkit-atm-cash-machine-key-press-2841.wav")
sound_4 = pygame.mixer.Sound("mixkit-atm-cash-machine-key-press-2841.wav")
sound_5 = pygame.mixer.Sound("mixkit-atm-cash-machine-key-press-2841.wav")
sound_6 = pygame.mixer.Sound("mixkit-atm-cash-machine-key-press-2841.wav")
sound_7 = pygame.mixer.Sound("mixkit-atm-cash-machine-key-press-2841.wav")
sound_8 = pygame.mixer.Sound("mixkit-atm-cash-machine-key-press-2841.wav")
sound_9 = pygame.mixer.Sound("mixkit-atm-cash-machine-key-press-2841.wav")
sound_10 = pygame.mixer.Sound("mixkit-atm-cash-machine-key-press-2841.wav")

# Set up mixer channels
channels = []  # Adjust based on your needs
for i in range(2):
        channels.append(pygame.mixer.Channel(i))
        
# Define the key-to-sound mapping
key_sound_mapping = {
	pygame.K_1: (sound_1, channels[0]),
	pygame.K_2: (sound_2, channels[1]),
	# Add more key mappings as needed
}

# Set up the display
pygame.display.set_caption("Raspiano Music")
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
                sound_to_play = key_sound_mapping[event.key][0]

                # Play the sound on all available channels with no delay
                for channel in channels:
                    if not channel.get_busy():
                        channel.play(sound_to_play, fade_ms=0)
                        break  # Play on the first available channel

    pygame.time.delay(10)  # Add a small delay to avoid high CPU usage

# Clean up pygame
pygame.quit()
