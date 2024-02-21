import pygame
import time

# Initialize Pygame for audio playback
pygame.init()

# Function to play music file and wait for it to finish
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(2)

# First part: Play the first music file and print message after completion
first_music_file = "bgm.mp3"  # Change this to your first music file path
play_music(first_music_file)
print("Kali is started")

# Second part: Play the second music file and display messages sequentially
second_music_file = "kalispeaks.mp3"  # Change this to your second music file path
pygame.mixer.music.load(second_music_file)
pygame.mixer.music.play()

# Display messages with some delay between them to simulate process steps
print("Starting mailer")
time.sleep(2)  # Wait for 2 seconds before the next message
print("Preparing to send mail")
time.sleep(2)  # Wait for 2 seconds before the next message
print("Sending mail")

# Wait for the second music to finish if it's still playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()
