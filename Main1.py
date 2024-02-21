import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Load and resize animation frames
frame_paths = ["kaliborn.png"]  # Add as many frames as you have
frames = [pygame.transform.scale(pygame.image.load(path), (screen_width, screen_height)) for path in frame_paths]
frame_count = len(frames)

# Function to play music file and wait for it to finish
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Function to play music and show animation with shaking effect
def play_music_and_animation(music_file, animation_frames, display_time=5):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    
    start_time = time.time()
    while pygame.mixer.music.get_busy() and (time.time() - start_time) < display_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                return
        
        # Create a shaking effect by randomly altering the position
        shake_intensity = 2  # Max pixels to move the image
        x_shake = random.randint(-shake_intensity, shake_intensity)
        y_shake = random.randint(-shake_intensity, shake_intensity)
        
        screen.fill((0, 0, 0))  # Fill the screen with black
        for current_frame in animation_frames:
            screen.blit(current_frame, (x_shake, y_shake))  # Draw the current frame with shake
        pygame.display.flip()  # Update the screen
        
        pygame.time.Clock().tick(21)  # Control frame rate for the shaking effect

# First part: Play the first music file without animation
#play_music("bgm.mp3")
print("Kali is started")

# Second part: Play the second music file with evil animation
play_music_and_animation("kalispeaks.mp3", frames, display_time=21)

# Display messages with delays to simulate process steps
print("Starting mailer")
time.sleep(2)
print("Preparing to send mail")
time.sleep(2)
print("Sending mail")

pygame.quit()
