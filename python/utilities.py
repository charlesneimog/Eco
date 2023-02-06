import math
import json
import os
from neoscore.common import *

GLOBALPITCHES = []

def getHOME_PATH():
    home = os.path.dirname(os.path.abspath(__file__))
    main_home = os.path.dirname(home)
    return main_home
    
def clear_global_notes():
    global GLOBALPITCHES
    GLOBALPITCHES = []
    return GLOBALPITCHES

def set_global_notes(nota):
    global GLOBALPITCHES
    if GLOBALPITCHES is None:
        GLOBALPITCHES = [nota]
    else:
        GLOBALPITCHES.append(nota)
    return "Global notes updated!"

def get_global_notes():
    global GLOBALPITCHES
    return GLOBALPITCHES

def my_ip():
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr + ":8000"

def UpdateRate(ms, blick, gesture, folder):
    json_data = {"update_rate": ms, "blick": blick, "name": gesture}
    with open(f'{folder}/update_rate.json', 'w') as out_file:
        json.dump(json_data, out_file, sort_keys = True, indent = 4, ensure_ascii = False)

def class2string(midiclass):
    return {
        0: 'c',
        1: 'c#',
        2: 'd',
        3: 'd#',
        4: 'e',
        5: 'f',
        6: 'f#',
        7: 'g',
        8: 'g#',
        9: 'a',
        10: 'a#',
        11: 'b',
    }[midiclass]
      
def string2midi(string):
    central_notes = {
        "cb": 59,
        "c": 60,
        "c#": 61,
        "db": 61,
        "d": 62,
        "d#": 63,
        "eb": 63,
        "e": 64,
        "f": 65,
        "f#": 66,
        "gb": 66,
        "g": 67,
        "g#": 68,
        "ab": 68,
        "a": 69,
        "a#": 70,
        "bb": 70,
        "b": 71,
        "cb": 71,
    }
    octave_up = string.count("'") * 12
    octave_down = string.count(",") * -12
    note = string.replace("'", "").replace(",", "")
    midi_note = central_notes[note] + octave_up + octave_down
    return midi_note
    
def midi2string(midi):
    central_notes = {
        "cb": 59,
        "c": 60,
        "c#": 61,
        "db": 61,
        "d": 62,
        "d#": 63,
        "eb": 63,
        "e": 64,
        "f": 65,
        "f#": 66,
        "gb": 66,
        "g": 67,
        "g#": 68,
        "ab": 68,
        "a": 69,
        "a#": 70,
        "bb": 70,
        "b": 71,
        "cb": 71,
    }
    # invert central notes 
    central_notes = {v: k for k, v in central_notes.items()}
    class_of_note = (midi % 12) + 60
    diff = midi - class_of_note
    # if diff is positive, add ' to the note
    if diff > 0:
        octave = "'" * (diff // 12)
    else:
        octave = "," * (diff // 12)
    return central_notes[class_of_note] + octave

def get_space_for_note(ratio):
    ratios = {
        '1/1': 80,
        '1/2': 40,
        '1/4': 20,
        '1/8': 10,
        '1/16': 6,
    }
    return ratios[ratio]
    
    
def freq2midi(freq):
    value = round(12 * (math.log2(freq) - math.log2(440.0)), 2) + 69
    return int(value * 100)

def get_octave(midicent):
    if midicent >= 2400 and midicent < 3600:
        return 1
    if midicent >= 3600 and midicent < 4800:
        return 2
    if midicent >= 4800 and midicent < 6000:
        return 3
    if midicent >= 6000 and midicent < 7200:
        return 4
    if midicent >= 7200 and midicent < 8400:
        return 5
    if midicent >= 8400 and midicent < 9600:
        return 6


def get_midi_class_of_midicent(midicent):
    midi = round(midicent / 100, 0)
    midi_modules = round(midicent / 100) % 12
    note_name = {
        0: 0, 
        1: 0,
        2: 2,
        3: 2,
        4: 4,
        5: 5,
        6: 5,
        7: 7,
        8: 7,
        9: 9,
        10: 9,
        11: 11, 
    }
    midi_class = midi2string(note_name[midi_modules])
    return midi_class, (midicent % 1200) - (note_name[midi_modules] * 100), midicent - (100 * midi)

def midialteration2symbol(alteration):
    if alteration < 6 and alteration > -6:
        return 'accidentalNatural'
    elif alteration < 56 and alteration > 44:
        return 'accidentalQuarterToneSharpStein'
    elif alteration < 106 and alteration > 94:
        return 'accidentalSharp'
    else:
        return None