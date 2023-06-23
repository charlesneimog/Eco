# import random
from neoscore.core.units import ZERO, Mm
from neoscore.core import neoscore
from neoscore.core.text import Text
# import NoteTablet
from neoscore.western.chordrest import NoteheadTable
from public.functions.utilities.utilities import *
from om_py import f2mc, mc2f, approx_mc
try:
    import pd
    pd_print = pd.print
except BaseException:
    pd_print = print

SAX_NOTES = []
SAX_AMPS = []


def set_SAX_global_notes(nota):
    global SAX_NOTES
    if SAX_NOTES is None:
        SAX_NOTES = [nota]
    else:
        SAX_NOTES.append(nota)
    return "Global notes updated!"


def set_SAX_global_amps(nota):
    global SAX_AMPS
    if SAX_AMPS is None:
        SAX_AMPS = [nota]
    else:
        SAX_AMPS.append(nota)
    return "Global amps updated!"


def get_SAX_global_notes():
    global SAX_NOTES
    if SAX_NOTES == [] or SAX_NOTES is None:
        # get 20 aleatory notes
        return random.sample(range(100, 1000), 20)
    else:
        return SAX_NOTES


def get_SAX_global_amps():
    global SAX_AMPS
    if SAX_AMPS == [] or SAX_AMPS is None:
        aleatoric_amps = random.sample(range(10, 200), 20)
        negative_amps = [x * -1 for x in aleatoric_amps]
        return negative_amps
    else:
        return SAX_AMPS


def clear_SAX_global_notes():
    global SAX_NOTES
    SAX_NOTES = []
    return "Global notes cleared!"


def clear_SAX_global_amps():
    global SAX_AMPS
    SAX_AMPS = []
    return "Global amps cleared!"

# ========================================
# ========================================
# ========================================


def SAX_midialteration2symbol(alteration):
    if alteration < 6 and alteration > -6:
        return ''
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


# =============================================
def SAX_add_articulation(figure, gesto, staff):  # TODO: remove staffs
    GESTOS = {
        'gesto1': [
            'articStaccatoAbove',
            'articAccentStaccatoAbove',
            'articTenutoAboveSmall'],
        'gesto2': [
            'articStaccatoAbove',
            'articTenutoAbove'],
        'gesto3': [
            'articMarcatoStaccatoAbove',
            'articAccentAboveSmall',
            'articTenutoAbove'],
    }
    articulations = GESTOS[gesto]
    MusicText(
        figure.extra_attachment_point,
        figure, random.choice(articulations),
        alignment_x=AlignmentX.CENTER,
        alignment_y=AlignmentY.CENTER,)
    return 'Articulation added!'

# =============================================


def SAX_8thTones(alteration):
    if alteration > 1100:
        alteration = alteration - 1200
    if alteration > -10 and alteration <= 10:
        return 'accidentalNatural'
    elif alteration > 10 and alteration <= 25:
        return 'accidentalNaturalOneArrowUp'
    elif alteration > 25 and alteration <= 40:
        return 'accidentalNaturalTwoArrowsUp'
    elif alteration > 40 and alteration <= 50:
        return 'accidentalNaturalThreeArrowsUp'
    elif alteration > 50 and alteration <= 60:
        return 'accidentalSharpThreeArrowsDown'
    elif alteration > 60 and alteration <= 75:
        return 'accidentalSharpTwoArrowsDown'
    elif alteration > 75 and alteration <= 90:
        return 'accidentalSharpOneArrowDown'
    elif alteration > 90 and alteration <= 110:
        return 'accidentalSharp'
    elif alteration > 110 and alteration <= 125:
        return 'accidentalSharpOneArrowUp'
    elif alteration > 125 and alteration <= 140:
        return 'accidentalSharpTwoArrowsUp'
    elif alteration > 140 and alteration <= 150:
        return 'accidentalSharpThreeArrowsUp'
    elif alteration > -30 and alteration <= -15:
        return 'accidentalNaturalOneArrowDown'
    elif alteration > -45 and alteration <= -30:
        return 'accidentalNaturalTwoArrowsDown'
    elif alteration > -55 and alteration <= -45:
        return 'accidentalNaturalThreeArrowsDown'
    elif alteration > -65 and alteration <= -55:
        return 'accidentalFlatThreeArrowsUp'
    elif alteration > -80 and alteration <= -65:
        return 'accidentalFlatTwoArrowsUp'
    elif alteration > -90 and alteration <= -80:
        return 'accidentalFlatOneArrowUp'
    elif alteration > -110 and alteration <= -90:
        return 'accidentalFlat'
    else:
        return ''


# ========================================
# ============= GESTOS ===================
# ============= GESTOS ===================
# ========================================

def SAX_gesto0():
    HOME = getHOME_PATH()
    default = neoscore.default_font  # Alias just for docs legibility
    sample = " The Score Player is ready! "
    Text((ZERO, Mm(180)), None, sample, default.modified(size=Unit(30)))
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/sax/gesto0.png',
        wait=True,
        dpi=300)
    UpdateRate(0, 0, f'{HOME}/sax/sax.json')
    return "Gesto 0 Rendered!"


def SAX_gesto1():
    pd_print("SAX_gesto1")
    HOME = getHOME_PATH()
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    staff.unit(7)
    Chordrest(Mm(35), staff, None, (1, 1))
    Clef(ZERO, staff, 'treble')
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/sax/gesto1.png',
        wait=True,
        dpi=600)
    UpdateRate(6000, 1, f'{HOME}/sax/sax.json')
    pd_print("SAX_gesto1 - Gesto 1 Rendered!")
    return "Gesto 1 Rendered!"


def SAX_gesto2():
    pd_print("SAX_gesto2")
    HOME = getHOME_PATH()
    PITCHES = get_SAX_global_notes()
    AMPS = get_SAX_global_amps()
    PITCHES, AMPS = FreqsAndAmps_InsideRange(PITCHES, AMPS, 7200, 9300)
    if PITCHES is None or PITCHES is []:
        PITCHES = aleatoric_freqs(40, 7200, 9300)
        AMPS = random.sample(range(-10, -200), 40)
    if len(PITCHES) != len(AMPS):
        return None
    # sort amps ascending
    sorted_amp = sorted(AMPS, reverse=True)
    index = 7
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(6100)

        try:
            sorted_amp = sorted(AMPS, reverse=True)
            amp_8th = sorted_amp[index]
            pd_print(f'index: {index}')
            index_8th_amp = AMPS.index(amp_8th)
            pitch_8th = PITCHES[index_8th_amp]
            break
        except BaseException:
            index -= 1
            continue
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    staff.unit(7)
    space = 10
    Clef(ZERO, staff, 'treble')
    midicent = f2mc(pitch_8th) + 200  # SAX SOPRANO TRANSPOSITION
    midicent = approx_mc(midicent)
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    wait_good_alteration = True
    while wait_good_alteration:
        alterations = SAX_midialteration2symbol(midi_alterations)
        if alterations is not None:
            octave = get_octave(midicent)
            note = [(pitch, alterations, octave)]  # TODO: Add alterations
            note = Chordrest(Mm(space), staff, note, (int(1), int(1)))
            Hairpin((ZERO, staff.unit(6)), note, (staff.unit(35), ZERO))
            POSITION = Unit(29)
            Dynamic((POSITION, staff.unit(10)), staff, "p")
            POSITION = Unit(200)
            Dynamic((POSITION, staff.unit(10)), staff, 'ffff')
            wait_good_alteration = False

    # just show image, without page
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/sax/gesto2.png',
        wait=True,
        dpi=600)
    UpdateRate(3000, 2, f'{HOME}/sax/sax.json')
    pd_print('SAX_gesto2: Rendered!')
    return "Gesto 2 Rendered!"


# ============================================
def SAX_gesto3():
    pd_print("SAX_gesto3")
    HOME = getHOME_PATH()
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    staff.unit(7)
    Chordrest(Mm(35), staff, None, (1, 1))
    Clef(ZERO, staff, 'treble')
    UpdateRate(15000, 3, f'{HOME}/sax/sax.json')
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/sax/gesto3.png',
        wait=True,
        dpi=900)
    pd_print("SAX_gesto3 - Gesto 3 Rendered!")
    return "Gesto 3 Rendered!"

# ============================================


def SAX_gesto4():
    pd_print('SAX_gesto4')
    home = getHOME_PATH()
    pitches = get_SAX_global_notes()
    amps = get_SAX_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        # if C3 is 4800 Eb2 is 3900
        pitches = aleatoric_freqs(40, 3900, 6000)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    numberOfIntations = 0
    while True:
        numberOfIntations += 1
        if numberOfIntations > 100:
            pitch, midi_alterations, cents = get_midi_class_of_midicent(6100)
        try:
            sorted_amp = sorted(amps, reverse=True)
            amp_8th = sorted_amp[index]
            index_8th_amp = amps.index(amp_8th)
            pitch_8th = pitches[index_8th_amp]
            break
        except BaseException:
            index -= 1
            continue
    pitchHz = pitch_8th
    midicent = f2mc(pitchHz)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            midicent = 5700

        if midicent > 6000:
            midicent = midicent - 1200
        elif midicent < 3900:
            midicent = midicent + 1200
        else:
            break
    # NOTE: BARITONE TRANSPOSITION
    pitchHz = mc2f(midicent)
    midicent = 2100 + midicent
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = SAX_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble'
    Clef(ZERO, staff, saxClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(40), staff.unit(-6.5)), staff, "tremolo3", scale=0.8)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicMP", scale=0.8)
    MusicText((Unit(70), staff.unit(-6.3)), staff,
              "dynamicFortePiano", scale=0.8)

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 5)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/sax/gesto4.png',
        wait=True,
        dpi=600)
    UpdateRate(
        17000,
        4,
        f'{home}/sax/sax.json',
        frequencyTarget=pitchHz,
        tupletDuration=1600,
        startPlay=9000)
    pd_print('SAX_gesto4: Rendered!')
    return "Gesto 4 Rendered!"

# ============================================


def SAX_gesto5():
    pd_print("SAX_gesto5")
    HOME = getHOME_PATH()
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    staff.unit(7)
    Chordrest(Mm(35), staff, None, (1, 1))
    Clef(ZERO, staff, 'treble')
    UpdateRate(22000, 5, f'{HOME}/sax/sax.json')
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/sax/gesto5.png',
        wait=True,
        dpi=600)
    return "Gesto 5 Rendered!"

# ============================================


def SAX_gesto6():
    pd_print('SAX_gesto6')
    home = getHOME_PATH()
    pitches = get_SAX_global_notes()
    amps = get_SAX_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3900, 6000)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(5700)
        try:
            sorted_amp = sorted(amps, reverse=True)
            amp_8th = sorted_amp[index]
            index_8th_amp = amps.index(amp_8th)
            pitch_8th = pitches[index_8th_amp]
            break
        except BaseException:
            index -= 1
            continue
    pitchHz = pitch_8th
    midicent = f2mc(pitchHz)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            midicent = 5700

        if midicent < 3900:
            midicent = midicent + 1200
        elif midicent > 6000:
            midicent = midicent - 1200
        else:
            break
    midicent = 2100 + midicent # transpotiion
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = SAX_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble'
    Clef(ZERO, staff, saxClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicPP", scale=0.8)
    MusicText((Unit(70), staff.unit(-6.3)), staff, "dynamicFF", scale=0.8)

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 5)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/sax/gesto6.png',
        wait=True,
        dpi=600)
    UpdateRate(
        13000,
        6,
        f'{home}/sax/sax.json',
        frequencyTarget=pitchHz,
        tupletDuration=1166,
        startPlay=1166)
    pd_print('SAX_gesto6: Rendered!')
    return "Gesto 6 Rendered!"

# ============================================


def SAX_gesto7():
    pd_print('SAX_gesto7')
    home = getHOME_PATH()
    pitches = get_SAX_global_notes()
    amps = get_SAX_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3900, 6000)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(5500)
            break
        try:
            sorted_amp = sorted(amps, reverse=True)
            amp_8th = sorted_amp[index]
            index_8th_amp = amps.index(amp_8th)
            pitch_8th = pitches[index_8th_amp]
            break
        except BaseException:
            index -= 1
            continue
    pitchHz = pitch_8th
    midicent = f2mc(pitchHz)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            midicent = 5500
            break

        if midicent < 3900:
            midicent = midicent + 1200
        elif midicent > 6000:
            midicent = midicent - 1200
        else:
            break
    midicent = 2100 + midicent
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = SAX_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble'
    Clef(ZERO, staff, saxClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(40), staff.unit(-6.5)), staff, "tremolo3", scale=0.8)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicMP", scale=0.8)
    MusicText((Unit(70), staff.unit(-6.3)), staff,
              "dynamicFortePiano", scale=0.8)

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 5)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/sax/gesto7.png',
        wait=True,
        dpi=600)
    UpdateRate(
        8000,
        7,
        f'{home}/sax/sax.json',
        frequencyTarget=pitchHz,
        tupletDuration=800,
        startPlay=0)
    pd_print('SAX_gesto7: Rendered!')
    return "Gesto 7 Rendered!"

# ============================================


def SAX_gesto8():
    pd_print('SAX_gesto8')
    home = getHOME_PATH()
    pitches = get_SAX_global_notes()
    amps = get_SAX_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3900, 6000)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(5300)
            break
        try:
            sorted_amp = sorted(amps, reverse=True)
            amp_8th = sorted_amp[index]
            index_8th_amp = amps.index(amp_8th)
            pitch_8th = pitches[index_8th_amp]
            break
        except BaseException:
            index -= 1
            continue
    pitchHz = pitch_8th
    midicent = f2mc(pitchHz)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            midicent = 5300
            break

        if midicent < 3900:
            midicent = midicent + 1200
        elif midicent > 6000:
            midicent = midicent - 1200
        else:
            break
    midicent = 2100 + midicent
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = SAX_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble'
    Clef(ZERO, staff, saxClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(40), staff.unit(-6.5)), staff, "tremolo3", scale=0.8)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicMP", scale=0.8)
    MusicText((Unit(70), staff.unit(-6.3)), staff,
              "dynamicFortePiano", scale=0.8)

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 5)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/sax/gesto8.png',
        wait=True,
        dpi=600)
    UpdateRate(
        7000,
        8,
        f'{home}/sax/sax.json',
        frequencyTarget=pitchHz,
        tupletDuration=1167,
        startPlay=0)
    pd_print('SAX_gesto8: Rendered!')
    return "Gesto 8 Rendered!"

# ============================================


def SAX_gesto9():
    home = getHOME_PATH()
    pitches = get_SAX_global_notes()
    amps = get_SAX_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3900, 6000)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(5200)
            break


        try:
            sorted_amp = sorted(amps, reverse=True)
            amp_8th = sorted_amp[index]
            index_8th_amp = amps.index(amp_8th)
            pitch_8th = pitches[index_8th_amp]
            break
        except BaseException:
            index -= 1
            continue
    pitchHz = pitch_8th
    midicent = f2mc(pitchHz)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            midicent = 5200
            break

        if midicent < 3900:
            midicent = midicent + 1200
        elif midicent > 6000:
            midicent = midicent - 1200
        else:
            break
    midicent = 2100 + midicent
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = SAX_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble'
    Clef(ZERO, staff, saxClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(40), staff.unit(-6.5)), staff, "tremolo3", scale=0.8)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicMP", scale=0.8)
    MusicText((Unit(70), staff.unit(-6.3)), staff,
              "dynamicFortePiano", scale=0.8)

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 5)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/sax/gesto9.png',
        wait=True,
        dpi=600)
    UpdateRate(
        23000,
        9,
        f'{home}/sax/sax.json',
        frequencyTarget=pitchHz,
        tupletDuration=1438,
        startPlay=0)
    pd_print('SAX_gesto9: Rendered!')
    return "Gesto 9 Rendered!"

# ============================================


def SAX_gesto10():
    pd_print('SAX_gesto10')
    home = getHOME_PATH()
    pitches = get_SAX_global_notes()
    amps = get_SAX_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3900, 6000)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(5800)
        try:
            sorted_amp = sorted(amps, reverse=True)
            amp_8th = sorted_amp[index]
            index_8th_amp = amps.index(amp_8th)
            pitch_8th = pitches[index_8th_amp]
            break
        except BaseException:
            index -= 1
            continue
    pitchHz = pitch_8th
    midicent = f2mc(pitchHz)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            midicent = 5800
            break
        if midicent < 3900:
            midicent = midicent + 1200
        elif midicent > 6000:
            midicent = midicent - 1200
        else:
            break
    midicent = 2100 + midicent
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = SAX_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble'
    Clef(ZERO, staff, saxClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(40), staff.unit(-6.5)), staff, "tremolo3", scale=0.8)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicMP", scale=0.8)
    MusicText((Unit(70), staff.unit(-6.3)), staff,
              "dynamicFortePiano", scale=0.8)

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 5)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/sax/gesto10.png',
        wait=True,
        dpi=600)
    UpdateRate(
        12000,
        10,
        f'{home}/sax/sax.json',
        frequencyTarget=pitchHz,
        tupletDuration=2000,
        startPlay=0)
    pd_print('SAX_gesto10: Rendered!')
    return "Gesto 10 Rendered!"

# ============================================


def SAX_gesto11():
    pd_print('SAX_gesto11')
    home = getHOME_PATH()
    pitches = get_SAX_global_notes()
    amps = get_SAX_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3900, 6000)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(5400)
            break
        try:
            sorted_amp = sorted(amps, reverse=True)
            amp_8th = sorted_amp[index]
            index_8th_amp = amps.index(amp_8th)
            pitch_8th = pitches[index_8th_amp]
            break
        except BaseException:
            index -= 1
            continue
    pitchHz = pitch_8th
    midicent = f2mc(pitchHz)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            midicent = 5400
            break
        if midicent < 3900:
            midicent = midicent + 1200
        elif midicent > 6000:
            midicent = midicent - 1200
        else:
            break
    midicent = 2100 + midicent
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = SAX_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble'
    Clef(ZERO, staff, saxClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(40), staff.unit(-6.5)), staff, "tremolo3", scale=0.8)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicMP", scale=0.8)
    MusicText((Unit(70), staff.unit(-6.3)), staff,
              "dynamicFortePiano", scale=0.8)

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 5)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/sax/gesto11.png',
        wait=True,
        dpi=600)
    UpdateRate(
        31000,
        11,
        f'{home}/sax/sax.json',
        frequencyTarget=pitchHz,
        tupletDuration=1823,
        startPlay=0)
    pd_print('SAX_gesto11: Rendered!')
    return "Gesto 11 Rendered!"


# ============================================
def SAX_gesto12():
    pd_print('SAX_gesto12')
    home = getHOME_PATH()
    pitches = get_SAX_global_notes()
    amps = get_SAX_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3900, 6000)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(5100)
            break
        try:
            sorted_amp = sorted(amps, reverse=True)
            amp_8th = sorted_amp[index]
            index_8th_amp = amps.index(amp_8th)
            pitch_8th = pitches[index_8th_amp]
            break
        except BaseException:
            index -= 1
            continue
    pitchHz = pitch_8th
    midicent = f2mc(pitchHz)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            midicent = 5100
            break
        if midicent < 3900:
            midicent = midicent + 1200
        elif midicent > 6000:
            midicent = midicent - 1200
        else:
            break
    midicent = 2100 + midicent
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = SAX_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble'
    Clef(ZERO, staff, saxClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(40), staff.unit(-6.5)), staff, "tremolo3", scale=0.8)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicMP", scale=0.8)
    MusicText((Unit(70), staff.unit(-6.3)), staff,
              "dynamicFortePiano", scale=0.8)

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 5)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/sax/gesto12.png',
        wait=True,
        dpi=600)
    UpdateRate(
        11000,
        12,
        f'{home}/sax/sax.json',
        frequencyTarget=pitchHz,
        tupletDuration=1571,
        startPlay=0)
    pd_print('SAX_gesto12: Rendered!')
    return "Gesto 12 Rendered!"
