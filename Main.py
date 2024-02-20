import pygame
import sys

# Initialize Pygame for audio playback
pygame.init()

# Load the audio file
audio_file = "bgm.mp3"  # Change this to the path of your audio file
pygame.mixer.music.load(audio_file)

# Play the audio
pygame.mixer.music.play()

# Display the message
print("Starting Kali AI Mailer...")

# Keep the program running until the audio playback is finished
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()
