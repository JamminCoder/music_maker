from utils import get_note_map, play_tone
import threading
import time

class Note:
    threads = []
    def join_threads():
        for thread in Note.threads:
            thread.join()

    def __init__(self, note, duration=1):
        # Ensures the first character of note is uppercase
        

        main_note = note[0].upper()
        self.note = main_note + note[1:]
        self.duration = duration
        self.rest = False
        if note == 'rest':
            self.rest = True
            return

        self.note_map = get_note_map()
        self.frequency = self.note_map[self.note]
    
    def play(self, speaker=None):
        if self.rest:
            time.sleep(self.duration)
            return
            
        play_tone(self.frequency, duration=self.duration, speaker=speaker)

    def play_threaded(self):
        thread = threading.Thread(target=self.play)
        Note.threads.append(thread)
        thread.start()
        