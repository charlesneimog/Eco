import random
import os
from neoscore.common import *
from neoscore.core.units import ZERO, Mm, Unit
from neoscore.core import neoscore
from neoscore.core.text import Text
from neoscore.western.chordrest import NoteheadTable
from python.utilities import *

def GUITAR_add_articulation(figure, gesto, staff):
    GESTOS = {
        'gesto1': ['articStaccatoAbove', 'articAccentStaccatoAbove'],
        'gesto2': ['articStaccatoAbove', 'articTenutoAbove'],
    }
    articulations = GESTOS[gesto]
    MusicText(figure.extra_attachment_point, figure, random.choice(articulations), alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
       
def GUITAR_add_dynamic(space, staff, gesto):
    DYNAMICS = {
        'gesto1': ['f', 'ff'],
        'gesto2': ['p', 'pp', 'mf'],
    }
    dynamic_random = random.choice([True, False])
    if dynamic_random:
        Dynamic((Mm(space), staff.unit(12)), staff, random.choice(DYNAMICS[gesto]))


# ========================================
# ========================================
# ========================================

def GUITAR_gesto0():
    HOME = getHOME_PATH()
    default = neoscore.default_font # Alias just for docs legibility
    sample = "The Score Player is ready!"
    Text((ZERO, Mm(180)), None, sample, default.modified(size=Unit(30)))
    UpdateRate(0, 1, 'gesto0', f'{HOME}/web-page/html/flute/')
    neoscore.render_image(rect=None, dest=f'{HOME}/web-page/html/flute/score.png', wait=False)
    return "Gesto 0 Rendered!"

def GUITAR_gesto1():
    HOME = getHOME_PATH()
    try:
        os.remove(f'{HOME}/web-page/html/guitar/score.png')
    except:
        pass
    # PITCHES = get_global_notes()
    PITCHES = [440, 220, 261, 285, 293]
    staff = Staff(ORIGIN, None, Mm(180))
    staff.unit(7)
    Clef(ZERO, staff, 'treble_8vb')
    Chordrest(Mm(10), staff, None, (1, 4))
    ratio = '1/1'
    spaces = [13, 13, 13, 6, 6, 6, 6]
    score_space = 10 + get_space_for_note('1/4')
    GUITAR_add_dynamic(score_space, staff, 'gesto1')
    MetronomeMark((ZERO, staff.unit(-6)), staff, [], "Seguir Métrica!")
    GESTO2_TABLE = NoteheadTable("noteheadBlack", "noteheadBlack", "noteheadBlack", "noteheadBlack")
    GESTO2_TABLE_II = NoteheadTable("noteheadTriangleRightWhite", "noteheadTriangleRightWhite", "noteheadTriangleRightWhite", "noteheadTriangleRightWhite")
    for space in spaces:
        alterations = None
        while alterations == None:
            PITCH = random.choice(PITCHES)
            nume, deno = ratio.split('/')
            thenote, midi_alterations, cents = get_midi_class_of_midicent(freq2midi(PITCH))
            alterations = midialteration2symbol(midi_alterations)
        octave = get_octave(freq2midi(PITCH))
        note = [(thenote, alterations, octave)]
        random_number = random.randint(0, 100)
        if random_number > 70:
            figure = Chordrest(Mm(score_space), staff, note, (int(nume), int(deno)), table=GESTO2_TABLE_II)
        else:
            figure = Chordrest(Mm(score_space), staff, note, (int(nume), int(deno)), table=GESTO2_TABLE)
            GUITAR_add_articulation(figure, gesto='gesto2', staff=staff)
        score_space += space
    UpdateRate(8000, 0, "gesto1", f'{HOME}/web-page/html/guitar/')    
    neoscore.render_image(rect=None, dest=f'{HOME}/web-page/html/guitar/score.png', wait=False)
    return "Gesto 1 Rendered!"
    

def GUITAR_gesto2():
    "Here, all notes must be played freely."
    HOME = getHOME_PATH()
    try:
        os.remove(f'{HOME}/web-page/html/guitar/score.png')
    except:
        pass
    PITCHES = get_global_notes()
    staff = Staff(ORIGIN, None, Mm(180))
    staff.unit(7)
    Clef(ZERO, staff, 'treble')
    MetronomeMark((ZERO, staff.unit(-6)), staff, [], "Gesture Thinking...")
    ratios = ['1/1']
    space = 10
    for PITCH in random.sample(PITCHES, len(PITCHES)):
        if space > (170 - 10):
            break
        else:
            ratio = random.choice(ratios)
            nume, deno = ratio.split('/')
            thenote, midi_alterations, cents = get_midi_class_of_midicent(freq2midi(PITCH))
            alterations = midialteration2symbol(midi_alterations)
            if alterations == None or freq2midi(PITCH) > 8400:
                pass
            else:
                octave = get_octave(freq2midi(PITCH))
                GESTO2_TABLE = NoteheadTable("noteheadBlack", "noteheadBlack", "noteheadBlack", "noteheadBlack")
                note = [(thenote, alterations, octave)]      
                figure = Chordrest(Mm(space), staff, note, (int(nume), int(deno)), table=GESTO2_TABLE)
                GUITAR_add_articulation(figure, gesto='gesto2', staff=staff)
                space += get_space_for_note('1/4')
    UpdateRate(12000, 1, "gesto2", f'{HOME}/web-page/html/guitar/')
    neoscore.render_image(rect=None, dest=f'{HOME}/web-page/html/guitar/score.png', wait=False)
    return "Gesto 2 Rendered!"


    
