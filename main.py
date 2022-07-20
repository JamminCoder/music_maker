import pygame
pygame.init()
from Note import Note
from Track import Track


BPM = 250
beat = 60 / BPM



def intro():
    return [
        Note('d5', beat),
        Note('d6', beat),
        Note('a5', beat),
        Note('g5', beat),
        Note('g6', beat),
        Note('a5', beat),
        Note('f#6', beat),
        Note('a5', beat)
    ]

def intro_lyrics():
    return [
        Note('a5', beat),
        Note.rest(beat / 4),
        Note('a5', beat),
        Note.rest(beat / 4),
        Note('a5', beat * 3),

        Note('g5', beat),
        Note('f#5', beat),
        Note('g5', beat * 2),
        Note('a5', beat),
        Note('f#5', beat * 2),
        Note('e5', beat),
        Note('d5', beat),
        Note('g5', beat * 2),
        Note('f#5', beat),
        Note('d5', beat),

        Note('g5', beat * 2),
        Note('f#5', beat),
        Note('d5', beat),

        Note('g5', beat * 2),
        Note('f#5', beat),
        Note('d5', beat * 2),

        Note('g5', beat * 2),
        Note('f#5', beat),
        Note('d5', beat),


        Note('g5', beat * 2),
        Note('g5', beat * 2),
        Note('g5', beat),
        Note('f#5', beat * 3)
    ]

intro2 = intro()
intro2[0] = Note('e5', beat)

intro3 = intro()
intro3[0] = Note('g5', beat)



sweet_child_o_mine = [
    *intro(),
    *intro(),

    *intro2,
    *intro2,

    *intro3,
    *intro3,

    *intro(),
    *intro(),

    *intro(),
    *intro(),

    *intro2,
    *intro2,

    *intro3,
    *intro3,

    Note('e6', beat),
    Note('a5', beat),
    Note('d6', beat),
    Note('a5', beat),
    Note('e6', beat),
    Note('a5', beat),
    Note('f#6', beat),
    Note('a5', beat),
    Note('g6', beat),
    Note('a5', beat),
    Note('f#6', beat),
    Note('a5', beat),
    Note('e6', beat),
    Note('a5', beat),
    Note('d6', beat),

    *intro_lyrics(),
    Note.rest(beat * 2),
    *intro_lyrics(),
    
    Note.rest(beat * 2),
    Note('a5', beat * 3),
    Note.rest(beat),
    Note('g5', beat),
    Note.rest(beat),
    Note('f#5', beat),
    Note.rest(beat),
    Note('g5', beat),
    Note.rest(beat),
    Note('d5', beat * 2),
    Note('e5', beat * 2),
    Note('f#5', beat),
    Note('d5', beat * 2),

    Note.rest(beat * 2),
    Note('a5', beat * 3),
    Note.rest(beat),
    Note('g5', beat),
    Note.rest(beat),
    Note('f#5', beat),
    Note.rest(beat),
    Note('g5', beat),
    Note.rest(beat),
    Note('d5', beat * 2),
    Note('e5', beat * 2),
    Note('f#5', beat),
    Note('d5', beat * 2),
]

def get_base_notes():
    return [
        Note('d4', beat * 3),
        Note('f#4', beat * 3),
        Note('g4', beat * 3),
        Note('a4', beat * 2),
        Note('g4', beat * 2),
        Note('f#4', beat),
        Note('d4', beat * 2),


        Note('c4', beat * 3),
        Note('e4', beat * 3),
        Note('f4', beat * 3),
        Note('g4', beat * 2),
        Note('f4', beat * 2),
        Note('e4', beat),
        Note('g3', beat * 4),

        Note('g4', beat),
        Note('f#4', beat),
        Note('d4', beat),
        Note('g4', beat),
        Note('f#4', beat),
        Note('d4', beat),
        Note('d4', beat * 4)
    ]



base = [
    *get_base_notes(),
    *get_base_notes(),
    *get_base_notes()
]


track_1 = Track(sweet_child_o_mine, speaker='r')
base_track = Track(base, speaker='l')

track_1.play()
base_track.play()

track_1.stop()
base_track.stop()


pygame.quit()