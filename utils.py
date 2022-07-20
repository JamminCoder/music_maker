from concurrent.futures import thread
import math
import numpy
import time
import pygame
from pygame.locals import *
import json



pygame.init()

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def read_json(path):
    return json.loads(read_file(path))

def get_note_map():
    return read_json('frequency_map.json')

def play_tone(frequency, sample_rate=44100, duration=1, speaker=None):
    """
    Play tone code taken and modified from https://stackoverflow.com/a/16268034
    """

    bits = 16
    pygame.mixer.pre_init(sample_rate, bits, 2)

    n_samples = int(round(duration * sample_rate))

    #setup our numpy array to handle 16 bit ints, which is what we set our mixer to expect with "bits" up above
    buf = numpy.zeros((n_samples, 2), dtype = numpy.int16)
    max_sample = 2**(bits - 1) - 1

    for s in range(n_samples):
        t = float(s) / sample_rate    # time in seconds

        #grab the x-coordinate of the sine wave at a given time, while constraining the sample to what our mixer is set to with "bits"
        sin_x = int(round(max_sample * math.sin(2 * math.pi * frequency * t)))

        # Control which speaker to play the sound from
        if not speaker:
            buf[s][0] = sin_x # left
            buf[s][1] = sin_x  # right
       
        elif speaker == 'r':
            buf[s][1] = sin_x
        elif speaker == 'l':
            buf[s][0] = sin_x

    sound = pygame.sndarray.make_sound(buf)
    one_sec = 1000 # Milliseconds
    sound.play(loops = 1, maxtime=int(duration * one_sec))
    time.sleep(duration)



NOTE_MAP = read_json('frequency_map.json')
    