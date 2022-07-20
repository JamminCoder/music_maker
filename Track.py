import threading

class Track:
    def __init__(self, notes_array, speaker=None):
        self.notes_array = notes_array
        self.thread = None
        self.speaker = speaker

    def play(self):
        def play_notes():
            for note in self.notes_array:
                if note is None:
                    continue
                
                note.play(speaker=self.speaker)

        self.thread = threading.Thread(target=play_notes)
        self.thread.start()

    def stop(self):
        self.thread.join()