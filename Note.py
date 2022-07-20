from utils import NOTE_MAP
from play_tone import Tone
import threading
import time


class Note:
    def __init__(self, note, duration=1):
        # Ensures the first character of note is uppercase
        main_note = note[0].upper()
        self.note = main_note + note[1:]
        self.duration = duration
        self.frequency = NOTE_MAP[self.note]
    
    def play(self, speaker=None):
        Tone.sine(self.frequency, duration=self.duration, speaker=speaker)

    @staticmethod
    def rest(duration):
        time.sleep(duration)

    @staticmethod
    def play_chord(notes):
        threads = []
        for note in notes:
            thread = threading.Thread(target=note.play)
            threads.append(thread)
        
        for thread in threads:
            thread.start()
        
        for thread in threads:
            thread.join()
        
