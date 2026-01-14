import pygame
from pathlib import Path


# This will generally be the mapping of the key on the keyboard -> piano

'''
Unsure for how I plan on doing this, but the general idea is to have keys [1,2,3,4,5,6,7,8,9,0,-,=].

I will then add a button to increase or decrease the octave by 1, or have an AUTO octave tracker depending on the sheet note.
'''

# Default octave
OCTAVE = 4
MIN_OCTAVE = 1
MAX_OCTAVE = 7

NOTE_NAMES = [
    "c", "c#", "d", "d#", "e", "f",
    "f#", "g", "g#", "a", "a#", "b"
]

# Modify to preference
OCTAVE_SWITCH = [
    pygame.K_LEFTBRACKET, # Decrease OCTAVE by 1
    pygame.K_RIGHTBRACKET  # Increase OCTAVE by 1
]

# Modify to preference
KEY_TO_NOTE = {
    pygame.K_1      : 0,  # C
    pygame.K_2      : 1,  # C#
    pygame.K_3      : 2,  # D
    pygame.K_4      : 3,  # D#
    pygame.K_5      : 4,  # E
    pygame.K_6      : 5,  # F
    pygame.K_7      : 6,  # F#
    pygame.K_8      : 7,  # G
    pygame.K_9      : 8,  # G#
    pygame.K_0      : 9,  # A 
    pygame.K_MINUS  : 10, # A#
    pygame.K_EQUALS : 11, # B
}

# This grabs the filename of the note given the index and octave
def note_to_filename(note_index, octave):
    note = NOTE_NAMES[note_index]
    return f"{note}{octave}.ogg"

p = Path('C:\Dev\Piano-Project\Piano-Notes')

# This combines to the actual file path of the note
def note_to_path(note_index, octave):
    return p / note_to_filename(note_index, octave)

def octave_switch(switch_key):
    global OCTAVE

    print(f'Current OCTAVE: {OCTAVE}')

    if switch_key == OCTAVE_SWITCH[0]:
        if OCTAVE == MIN_OCTAVE:
            print('Cannot lower Octave')
        else:
            OCTAVE -= 1

    elif switch_key == OCTAVE_SWITCH[-1]:
        if OCTAVE == MAX_OCTAVE:
            print('Cannot increase Octave')
        else:
            OCTAVE += 1

    else:
        print("Not a recognized octave switch key")


def play_note(key, sounds, active_notes):
    global OCTAVE

    if key not in KEY_TO_NOTE:
        return 
    
    note_index = KEY_TO_NOTE[key]
    sound = sounds.get((note_index, OCTAVE))

    # It doesn't exist
    if sound is None:
        return
    
    note_id = (note_index, OCTAVE)

    channel = pygame.mixer.find_channel()

    if channel is None:
        return # no free voices
    
    channel.play(sound)
    active_notes[note_id] = channel

    print(f"Playing {NOTE_NAMES[note_index]}{OCTAVE}")

def release_note(key, active_notes):
    if key not in KEY_TO_NOTE:
        return
    
    note_index = KEY_TO_NOTE[key]
    note_id = (note_index, OCTAVE)

    channel = active_notes.pop(note_id, None)

    if channel:
        channel.fadeout(550)
        print(f"Note: {NOTE_NAMES[note_index]} released")



if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    # TEMP (necessary even if nothing is displayed)
    screen_width = 400
    screen_height = 300

    screen = pygame.display.set_mode((screen_width, screen_height))


    sounds = {} #(notes_index, octave)
    for octave in range(0, 8):
        for note_index in range(12):
            path = note_to_path(note_index, octave)
            if path.exists():
                sounds[(note_index, octave)] = pygame.mixer.Sound(path)

    active_notes = {}



    print(f"Loaded {len(sounds)} samples")
    for k in sorted(sounds.keys()):
        print(k, note_to_filename(k[0], k[-1]))