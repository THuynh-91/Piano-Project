import pygame
import time
import sys
from pathlib import Path
import os




def main():
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()

    p = Path('C:\Dev\Piano-Project\Piano-Notes')
    sound = os.path.join(p, 'a#1.ogg')

    # TEMP (necessary even if nothing is displayed)
    screen_width = 400
    screen_height = 300

    screen = pygame.display.set_mode((screen_width, screen_height))

    #pygame.display.set_caption("Key Press Sound Example")

    try:
        sound_effect = pygame.mixer.Sound(sound)
        
    except pygame.error as e:
        print(f"Cannot load sound file: {e}")
        sys.exit()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Checks for keyboard press (EXAMPLE FOR NOW)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if not sound_effect.get_num_channels():
                        print("s was pressed and A#1 is playing")
                        sound_effect.play(-1)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    print("s released  stop A#1 from playing")
                    sound_effect.fadeout(550)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()