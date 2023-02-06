import json
import os
from neoscore.common import *
import random
try:
    import pd
    pd_print = pd.print
except:
    pd_print = print 

from om_py import *


# freq2mc
GLOBALPITCHES = []

# ========================================
def getHOME_PATH():
    home = os.path.dirname(os.path.abspath(__file__))
    main_home = os.path.dirname(home)
    return main_home
    
# ========================================
def my_ip():
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return "https://" + IPAddr + ":8090"

# ========================================
def UpdateRate(measureDuration, gestureNumber, filePathname, frequencyTarget=0, tupletDuration=0, startPlay=0, gestRepetition=0.6, gestProb=0.0):
    ''' It updates the rate of the gesture '''
    # remove all things before '_'. gesto4 must be gesto4
    jsonData = {
                "measureDuration": measureDuration, 
                "gestureNumber": gestureNumber,
                "frequencyTarget": frequencyTarget,
                "tupletDuration": tupletDuration,
                "Name": f'gesto{gestureNumber}',
                "startPlay": startPlay,
                "gestRepetition": gestRepetition,
                "gestProb": gestProb
                }
    
    with open(filePathname, 'w') as outfile:
        json.dump(jsonData, outfile, sort_keys = True, indent = 4, ensure_ascii = False)

# ========================================
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
      
# ========================================

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
    
# ========================================
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


# ========================================
def get_space_for_note(ratio):
    ratios = {
        '1/1': 80,
        '1/2': 40,
        '1/4': 20,
        '1/8': 10,
        '1/12': 8,
        '1/16': 6,
        '1/32': 4,
    }
    return ratios[ratio]
   
# ========================================
def aleatoric_freqs(number_of_freqs, range_down_midicent, range_up_midicent):
    ''' It converts choose randomically a number of notes between two midicents,
    and returns a list of frequencies '''
    freqs = []
    for i in range(number_of_freqs):
        midicent = random.randint(range_down_midicent, range_up_midicent)
        freqs.append(mc2f(midicent))
    return freqs

# ========================================
def PitchesInsideRange(pitches, range_down, range_up):
    ''' It checks if all the pitches are inside the range '''
    if pitches is None or pitches == []:
        return []
    good_pitches = []
    for pitch in pitches:
        midicent = f2mc(pitch)
        midi_alterations = get_midi_class_of_midicent(midicent)[1]
        if midicent < range_up and midicent > range_down:
            good_pitches.append(pitch)
    return good_pitches

# ========================================
def FreqsInsideRange(pitches, range_down, range_up):
    ''' It checks if all the pitches are inside the range '''
    if pitches is None or pitches == []:
        return []
    good_pitches = []
    for pitch in pitches:
        midicent = f2mc(pitch)
        midi_alterations = get_midi_class_of_midicent(midicent)[1]
        if midicent < range_up and midicent > range_down:
            good_pitches.append(pitch)
    return good_pitches

# ========================================
def FreqsAndAmps_InsideRange(pitches, amps, range_down, range_up):
    ''' It checks if all the pitches are inside the range '''
    if pitches is None or pitches == []:
        return []
    good_pitches = []
    good_amps = []
    for pitch in pitches:
        midicent = f2mc(pitch)
        midi_alterations = get_midi_class_of_midicent(midicent)[1]
        if midicent < range_up and midicent > range_down:
            good_pitches.append(pitch)
            good_amps.append(amps[pitches.index(pitch)])
    if good_pitches == []:
        return [], []
    else:
        return good_pitches, good_amps 

# ========================================
def get_octave(midicent):
    if midicent >= 2400 and midicent < 3600:
        return 1
    if midicent >= 3600 and midicent < 4800:
        return 2
    if midicent >= 4800 and midicent < 6000:
        return 3
    if midicent >= 6000 and midicent < 7150:
        return 4
    if midicent >= 7150 and midicent < 8350:
        return 5
    if midicent >= 8350 and midicent < 9550:
        return 6
    if midicent >= 9550 and midicent < 10800:
        return 7
    if midicent >= 10800 and midicent < 12000:
        return 8

# ========================================
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
 
# ========================================
def midialteration2symbol(alteration):
    if alteration < 6 and alteration > -6:
        return ''
    elif alteration < 56 and alteration > 44:
        return 'accidentalQuarterToneSharpStein'
    elif alteration < 106 and alteration > 94:
        return 'accidentalSharp'
    else:
        return None
