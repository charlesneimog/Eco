import random
import os
from neoscore.common import *
from neoscore.core.units import ZERO, Mm
from neoscore.core import neoscore
from neoscore.core.text import Text
from neoscore.western.chordrest import NoteheadTable
from python.utilities import *

COMPOSING = False

def FLUTE_midialteration2symbol(alteration):
    # import pd 
    # pd.print(f'Alteration: {alteration}') 
    # Natural
    if alteration < 6 and alteration > -6:
        return 'accidentalNatural'
    
    # Flat
    elif alteration < -44 and alteration > -54:
        return 'accidentalQuarterToneFlatNaturalArrowDown'
    
    # Sharp
    elif alteration < 30 and alteration > 20:
        return 'accidentalQuarterToneSharpNaturalArrowUp'
    elif alteration < 56 and alteration > 44:
        return 'accidentalQuarterToneSharpStein'
    elif alteration < 75 and alteration > 65:
        return 'accidentalHalfSharpArrowUp'
    elif alteration < 106 and alteration > 94:
        return 'accidentalSharp'
    elif alteration < 130 and alteration > 120:
        return 'accidentalThreeQuarterTonesSharpArrowUp'
    
    else:
        return None


def FLUTE_add_articulation(figure, gesto, staff):
    GESTOS = {
        'gesto1': ['articStaccatoAbove', 'articAccentStaccatoAbove'],
        'gesto2': ['articStaccatoAbove', 'articTenutoAbove'],
    }
    articulations = GESTOS[gesto]
    MusicText(figure.extra_attachment_point, figure, random.choice(articulations), alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
       
def FLUTE_add_dynamic(space, staff, gesto):
    DYNAMICS = {
        'gesto1': ['f', 'mf', 'ff'],
        'gesto2': ['p', 'pp', 'fp'],
    }
    dynamic_random = random.choice([True, False])
    if dynamic_random:
        Dynamic((Mm(space), staff.unit(12)), staff, random.choice(DYNAMICS[gesto]))


# ========================================
# ========================================
# ========================================

def FLUTE_gesto0():
    HOME = getHOME_PATH()
    default = neoscore.default_font # Alias just for docs legibility
    sample = "The Score Player is ready!"
    Text((ZERO, Mm(180)), None, sample, default.modified(size=Unit(30)))
    UpdateRate(0, 1, 'gesto0', f'{HOME}/web-page/html/flute/')
    neoscore.render_image(rect=None, dest=f'{HOME}/web-page/html/flute/score.png', wait=False)
    return "Gesto 0 Rendered!"

def FLUTE_gesto1():
    HOME = getHOME_PATH()
    try:
        os.remove(f'{HOME}/web-page/html/flute/score.png')
    except:
        pass
    PITCHES = get_global_notes()
    # neoscore.setup()
    staff = Staff(ORIGIN, None, Mm(180))
    staff.unit(7)
    Clef(ZERO, staff, 'treble')
    space = 10
    ratios = ['1/4', '1/8', '1/16']
    FLUTE_add_dynamic(7, staff, gesto='gesto1')
    # check if pitch is list or not
    if isinstance(PITCHES, list):
        pass
    else:
        PITCHES = [PITCHES]
    
    while True:
        ratio = random.choice(ratios)
        nume, deno = ratio.split('/')
        if space > (170 - 10):
            break
        else:
            frequency = random.choice(PITCHES)
            if freq2midi(frequency) > 8400 or freq2midi(frequency) < 5900:
                pass
            else:
                thenote, midi_alterations, cents = get_midi_class_of_midicent(freq2midi(frequency))
                alterations = FLUTE_midialteration2symbol(midi_alterations)
                octave = get_octave(freq2midi(frequency))
                note = [(thenote, alterations, octave)] 
                figure = Chordrest(Mm(space), staff, note, (int(nume), int(deno)))
                FLUTE_add_articulation(figure, gesto='gesto1', staff=staff)
                space += get_space_for_note(ratio)
    UpdateRate(8000, 0, "gesto1", f'{HOME}/web-page/html/flute/')
    neoscore.render_image(rect=None, dest=f'{HOME}/web-page/html/flute/score.png', wait=False)
    return "Gesto 1 Rendered!"


def FLUTE_gesto2():
    "Here, all notes must be played freely."
    import pd
    HOME = getHOME_PATH()
    try:
        os.remove(f'{HOME}/web-page/html/flute/score.png')
    except:
        pass
    PITCHES = get_global_notes()
    staff = Staff(ORIGIN, None, Mm(180))
    staff.unit(7)
    Clef(ZERO, staff, 'treble')
    MetronomeMark((ZERO, staff.unit(-6)), staff, [], "Improvisar Gestualmente!")
    ratios = ['1/1']
    space = 10
    GESTO2_TABLE = NoteheadTable("noteheadBlack", "noteheadBlack", "noteheadBlack", "noteheadBlack")
    for PITCH in random.sample(PITCHES, len(PITCHES)):
        if space > (170 - 10):
            break
        else:
            ratio = random.choice(ratios)
            nume, deno = ratio.split('/')
            thenote, midi_alterations, cents = get_midi_class_of_midicent(freq2midi(PITCH))
            alterations = FLUTE_midialteration2symbol(midi_alterations)
            if alterations == None or freq2midi(PITCH) > 8400 or freq2midi(PITCH) < 5900:
                pass
            else:
                octave = get_octave(freq2midi(PITCH))
                note = [(thenote, alterations, octave)]   
                pd.print(f'note: {note}')   
                figure = Chordrest(Mm(space), staff, note, (int(nume), int(deno)), table=GESTO2_TABLE)
                FLUTE_add_articulation(figure, gesto='gesto2', staff=staff)
                space += get_space_for_note('1/4')
    UpdateRate(12000, 1, "gesto2", f'{HOME}/web-page/html/flute/')
    neoscore.render_image(rect=None, dest=f'{HOME}/web-page/html/flute/score.png', wait=False)
    return "Gesto 2 Rendered!"


    
