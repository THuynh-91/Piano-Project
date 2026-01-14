import conversion
import pygame
import sys

def main():
    pygame.init()
    pygame.mixer.init()

    # TEMP (necessary even if nothing is displayed)
    screen_width = 400
    screen_height = 300

    screen = pygame.display.set_mode((screen_width, screen_height))


    sounds = {} #(notes_index, octave)
    for octave in range(0, 8):
        for note_index in range(12):
            path = conversion.note_to_path(note_index, octave)
            if path.exists():
                sounds[(note_index, octave)] = pygame.mixer.Sound(path)

    active_notes = {}

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for eligible keyboard press
            elif event.type == pygame.KEYDOWN:

                if event.key in conversion.OCTAVE_SWITCH:
                    conversion.octave_switch(event.key)
                    
                elif event.key not in conversion.KEY_TO_NOTE:
                    print("This is not a set key")

                elif event.key in conversion.OCTAVE_SWITCH:
                    conversion.octave_switch(event.key)

                else:
                    conversion.play_note(event.key, sounds, active_notes)

            elif event.type == pygame.KEYUP:
                conversion.release_note(event.key, active_notes )
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


