from importlib.resources import is_resource
from utils import NOTE_MAP
from Tone import Tone
import threading
import time


class Note:
    def __init__(self, note, duration=1):
        self.duration = duration
        if note == 'rest':
            self.is_resting = True
            return
        else:
            self.is_resting = False

        # Ensures the first character of note is uppercase
        main_note = note[0].upper()
        self.note = main_note + note[1:]
        self.frequency = NOTE_MAP[self.note]
        
        
    
    def play(self, speaker=None):
        if not self.is_resting:
            Tone.sine(self.frequency, duration=self.duration, speaker=speaker)
        else:
            time.sleep(self.duration)

    @staticmethod
    def rest(duration):
        return Note('rest', duration)

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
        
