import random
from neoscore.core.units import ZERO, Mm, Unit
from neoscore.core import neoscore
from neoscore.core.text import Text
from neoscore.western.chordrest import NoteheadTable
from public.functions.utilities.utilities import *
from om_py import f2mc, approx_mc

try:
    import pd
    pd_print = pd.print
except BaseException:
    pd_print = print

GUITAR_NOTES = []
GUITAR_AMP = []


def set_GUITAR_global_notes(nota):
    global GUITAR_NOTES
    if GUITAR_NOTES is None:
        GUITAR_NOTES = [nota]
    else:
        GUITAR_NOTES.append(nota)
    return "Global notes updated!"


def set_GUITAR_global_amps(amp):
    global GUITAR_AMP
    if GUITAR_AMP is None:
        GUITAR_AMP = [amp]
    else:
        GUITAR_AMP.append(amp)
    return "Global amp updated!"


def get_GUITAR_global_notes():
    global GUITAR_NOTES
    if GUITAR_NOTES == [] or GUITAR_NOTES is None:
        # get 20 aleatory notes
        return random.sample(range(100, 1000), 20)
    else:
        return GUITAR_NOTES


def get_GUITAR_global_amps():
    global GUITAR_AMP
    if GUITAR_AMP == [] or GUITAR_AMP is None:
        aleatoric_amps = random.sample(range(10, 200), 20)
        negative_amps = [x * -1 for x in aleatoric_amps]
        return negative_amps
    else:
        return GUITAR_AMP


def clear_GUITAR_global_notes():
    global GUITAR_NOTES
    GUITAR_NOTES = []
    return "Global notes cleared!"


def clear_GUITAR_global_amps():
    global GUITAR_AMP
    GUITAR_AMP = []
    return "Global amp cleared!"


# ========================================

def GUITAR_midialteration2symbol(alteration):
    if alteration < 6 and alteration > -6:
        return 'accidentalNatural'

    elif alteration > -106 and alteration < -94:
        return 'accidentalFlat'

    elif alteration < 106 and alteration > 94:
        return 'accidentalSharp'

    elif alteration < 130 and alteration > 120:
        return 'accidentalThreeQuarterTonesSharpArrowUp'

    else:
        return None


def GUITAR_add_articulation(figure, gesto, staff):
    GESTOS = {
        'gesto1': ['pluckedSnapPizzicatoAbove'],
        'gesto2': ['articStaccatoAbove', 'articTenutoAbove'],
    }
    articulations = GESTOS[gesto]
    MusicText(
        figure.extra_attachment_point,
        figure,
        random.choice(articulations),
        alignment_x=AlignmentX.CENTER,
        alignment_y=AlignmentY.CENTER)

# ========================================


def GUITAR_add_dynamic(space, staff, gesto):
    DYNAMICS = {
        'gesto1': ['f', 'ff', 'sf'],
        'gesto2': ['p', 'pp', 'mf'],
    }
    dynamic_random = random.choice([True, False])
    if dynamic_random:
        Dynamic((Mm(space), staff.unit(12)), staff,
                random.choice(DYNAMICS[gesto]))

# ========================================


def GUITAR_check_pitches(pitches, min_midicent, max_midicent):
    good_pitches = []
    for pitch in pitches:
        midicent = f2mc(pitch)
        midi_alterations = get_midi_class_of_midicent(midicent)[1]
        if midicent < max_midicent and midicent > min_midicent and midi_alterations is not None:
            good_pitches.append(pitch)
    return good_pitches

# ========================================
# ========================================
# ========================================


def GUITAR_tremoloPosition(note, octave):
    if note == 'g' and octave == 3:
        return 5.5
    if note == 'b' and octave == 3:
        return 4.5
    if note == 'd' and octave == 4:
        return 3.5
    if note == 'f' and octave == 4:
        return 2.5
    if note == 'a' and octave == 4:
        return 1.5
    else:
        return 0


# =============================================
def GUITAR_8thTones(alteration):
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


def GUITAR_gesto0():
    HOME = getHOME_PATH()
    default = neoscore.default_font  # Alias just for docs legibility
    sample = " The Score is ready! "
    Text((ZERO, Mm(180)), None, sample, default.modified(size=Unit(30)))
    # UpdateRate(updateRate, gesture, file_pathname, frequencyTarget, tupletDuration)
    UpdateRate(0, 0, f'{HOME}/guitar/guitar.json', 1, 1)
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/guitar/gesto0.png',
        wait=True,
        dpi=300)
    return "Gesto 0 Rendered!"

# ========================================


def GUITAR_gesto1():
    pd_print("Guitar_gesto1")
    HOME = getHOME_PATH()
    GUITAR_NOTEHEAD = NoteheadTable(
        "noteheadSquareBlack",
        "noteheadSquareBlack",
        "noteheadSquareBlack",
        "noteheadSquareBlack")
    gesture_number = random.randint(2, 3)
    score_horizontal_position = 0
    if gesture_number == 2:
        text_position = (Mm(60), Mm(-15))
    elif gesture_number == 3:
        text_position = (Mm(100), Mm(-15))
    Text(text_position, None, 'Sobre a boca, seguir as alturas!',
         neoscore.default_font.modified(size=Unit(10), italic=True))
    iteration = 0
    while gesture_number > 0:
        gesture_number -= 1
        Path.rect((Mm(score_horizontal_position), Mm(-10)), None, Mm(80),
                  Mm(26), Brush(Color(255, 255, 255, 255)), Pen(thickness=Mm(0.5)))
        POSITION = (Mm(score_horizontal_position), Mm(0))
        notes_number = random.randint(4, 7)
        fixed_notes_number = notes_number
        staff = Staff(POSITION, None, Mm(80))
        staff.unit(7)
        corda = random.choice(['Corda 1', 'Corda 2', 'Corda 3'])
        STRING_TXT_POSITION = (Mm(score_horizontal_position + 3), Mm(-4))
        Text(
            STRING_TXT_POSITION,
            None,
            corda,
            neoscore.default_font.modified(
                size=Unit(10)))
        space = 10
        Clef(ZERO, staff, 'percussion_2')
        number_of_iterations = 0
        while notes_number > 0:
            notes_number -= 1
            pitch_octave = random.choice(
                [['g', 3], ['b', 3], ['d', 4], ['f', 4], ['a', 4]])
            pitch, octave = pitch_octave
            note = [(pitch, '', octave)]
            tremolo_position = Unit(3)  # positivo é pra diretira
            note = Chordrest(Mm(space), staff, note,
                             (int(1), int(1)), table=GUITAR_NOTEHEAD)
            staff_unit = GUITAR_tremoloPosition(pitch, octave)
            MusicText((tremolo_position, staff.unit(
                staff_unit)), note, "tremolo3")
            space += (70 / fixed_notes_number) * \
                (random.randint(50, 130) / 100)
            number_of_iterations += 1
            if number_of_iterations > 100:
                pd.print('GUITAR: Too many iterations!')
        score_horizontal_position += 90
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/guitar/gesto1.png',
        wait=True)
    UpdateRate(6000, 1, f'{HOME}/guitar/guitar.json', 1, 1)
    pd_print("Guitar_gesto1: Rendered!")
    return "Gesto 1 Rendered!"


def GUITAR_gesto2():
    pd_print("GUITAR_gesto2")
    HOME = getHOME_PATH()
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    staff.unit(7)
    Chordrest(Mm(35), staff, None, (1, 1))
    Clef(ZERO, staff, 'treble')
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/guitar/gesto2.png',
        wait=True,
        dpi=600)
    UpdateRate(3000, 2, f'{HOME}/guitar/guitar.json')
    pd_print("GUITAR_gesto2 - Gesto 2 Rendered!")
    return "Gesto 2 Rendered!"


def GUITAR_gesto3():
    pd_print("GUITAR_gesto3")
    HOME = getHOME_PATH()
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    staff.unit(7)
    Chordrest(Mm(35), staff, None, (1, 1))
    Clef(ZERO, staff, 'treble')
    UpdateRate(13000, 3, f'{HOME}/guitar/guitar.json')
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/guitar/gesto3.png',
        wait=True,
        dpi=300)
    pd_print("GUITAR_gesto3 - Gesto 3 Rendered!")
    return "Gesto 3 Rendered!"


def GUITAR_gesto4():
    pd_print("GUITAR_gesto4")
    HOME = getHOME_PATH()
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    staff.unit(7)
    Chordrest(Mm(35), staff, None, (1, 1))
    Clef(ZERO, staff, 'treble')
    UpdateRate(19000, 4, f'{HOME}/guitar/guitar.json')
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/guitar/gesto4.png',
        wait=True,
        dpi=600)
    pd_print("GUITAR_gesto4 - Gesto 4 Rendered!")
    return "Gesto 4 Rendered!"


def GUITAR_gesto5():
    pd_print('GUITAR_gesto5')
    home = getHOME_PATH()
    pitches = get_GUITAR_global_notes()
    amps = get_GUITAR_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 4000, 7600)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 4000, 7600)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble_8vb'
    Clef(ZERO, staff, saxClef)
    numberOfNotes = random.randint(2, 4)
    if numberOfNotes == 3:
        spacoBetweenNotes = 25
    elif numberOfNotes == 2:
        spacoBetweenNotes = 35
    elif numberOfNotes == 4:
        spacoBetweenNotes = 20
    spaco = 5
    for x in range(numberOfNotes):
        index = random.randint(1, 3)
        while True:
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
        midicent = approx_mc(pitchHz)
        iteration = 0
        while True:
            iteration += 1
            if iteration > 30:
                midicent = random.randint(7300, 7900)
                break
            if midicent > 6000:
                midicent = midicent - 1200
            elif midicent < 4000:
                midicent = midicent + 1200
            else:
                break
        midicent = approx_mc(midicent)
        pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
        alterations = GUITAR_8thTones(midi_alterations)
        octave = get_octave(midicent)
        pitch_info = [(pitch, alterations, octave)]
        Chordrest(Mm(spaco), staff, pitch_info, (int(1), int(1)))
        spaco = spaco + spacoBetweenNotes
        
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "s.p.", font)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicMP", scale=0.8)
    MusicText((Unit(70), staff.unit(-6.3)), staff, "dynamicSforzato", scale=0.8)
    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)

    # TODO: replace this code with new example provide by neoscore
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 3)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    neoscore.render_image(
        rect=None,
        dest=f'{home}/guitar/gesto5.png',
        wait=True,
        dpi=600)
    UpdateRate(
        22000,
        5,
        f'{home}/guitar/guitar.json',
        frequencyTarget=pitchHz,
        tupletDuration=1294)
    pd_print('GUITAR_gesto5: Rendered!')
    return "Gesto 5 Rendered!"

# ============================================

def GUITAR_gesto6():
    pd_print('GUITAR_gesto6')
    home = getHOME_PATH()
    pitches = get_GUITAR_global_notes()
    amps = get_GUITAR_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 4000, 7600)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 4000, 7600)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None

    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble_8vb'
    Clef(ZERO, staff, saxClef)
    numberOfNotes = random.randint(2, 4)
    spacoBetweenNotes = 20
    if numberOfNotes == 3:
        spacoBetweenNotes = 25
    elif numberOfNotes == 2:
        spacoBetweenNotes = 35
    elif numberOfNotes == 4:
        spacoBetweenNotes = 20
    spaco = 5
    for x in range(numberOfNotes):
        index = random.randint(1, 3)
        while True:
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
        midicent = approx_mc(f2mc(pitchHz))
        iteration = 0
        while True:
            iteration += 1
            if iteration > 30:
                midicent = random.randint(4400, 5900)
            if midicent > 6000:
                midicent = midicent - 1200
            elif midicent < 4000:
                midicent = midicent + 1200
            else:
                break
        midicent = midicent
        pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
        alterations = GUITAR_8thTones(midi_alterations)
        octave = get_octave(midicent)
        pitch_info = [(pitch, alterations, octave)]
        Chordrest(Mm(spaco), staff, pitch_info, (int(1), int(1)))
        spaco = spaco + spacoBetweenNotes
        
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

    # TODO: replace this code with new example provide by neoscore
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 3)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    neoscore.render_image(
        rect=None,
        dest=f'{home}/guitar/gesto6.png',
        wait=True,
        dpi=600)
    UpdateRate(
        11000,
        6,
        f'{home}/guitar/guitar.json',
        frequencyTarget=pitchHz,
        tupletDuration=1375, 
        gestProb=0.3,
        gestRepetition=1)
    pd_print('GUITAR_gesto6: Rendered!')
    return "Gesto 6 Rendered!"

# ============================================

def GUITAR_gesto7():
    pd_print('GUITAR_gesto7')
    home = getHOME_PATH()
    pitches = get_GUITAR_global_notes()
    amps = get_GUITAR_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 4000, 7600)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 4000, 7600)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 2)
    while True:
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
    midicent = approx_mc(f2mc(pitchHz))
    while True:
        if midicent > 7600:
            midicent = midicent - 1200
        elif midicent < 4000:
            midicent = midicent + 1200
        else:
            break
    midicent = midicent
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = GUITAR_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    guitarClef = 'treble_8vb'
    Clef(ZERO, staff, guitarClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(40), staff.unit(-6.5)), staff, "tremolo3", scale=0.8)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicPP", scale=0.8)
    MusicText((Unit(70), staff.unit(-6.3)), staff,
              "dynamicFortePiano", scale=0.8)
    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    # WARNING: replace this code with new example provide by neoscore
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 3)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/guitar/gesto7.png',
        wait=True,
        dpi=600)
    UpdateRate(
        7000,
        7,
        f'{home}/guitar/guitar.json',
        frequencyTarget=pitchHz,
        gestProb=0.05,
        gestRepetition=1,
        tupletDuration=780)
    pd_print('GUITAR_gesto7: Rendered!')
    return "Gesto 7 Rendered!"

# ============================================


def GUITAR_gesto8():
    pd_print('GUITAR_gesto8')
    home = getHOME_PATH()
    pitches = get_GUITAR_global_notes()
    amps = get_GUITAR_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 4000, 7600)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 4000, 7600)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 2)
    while True:
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
    while True:
        if midicent > 7600:
            midicent = midicent - 1200
        elif midicent < 4000:
            midicent = midicent + 1200
        else:
            break
    midicent = approx_mc(midicent)
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = GUITAR_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    guitarClef = 'treble_8vb'
    Clef(ZERO, staff, guitarClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(40), staff.unit(-6.5)), staff, "pluckedSnapPizzicatoAbove", scale=0.8)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicFF", scale=0.8)
    Text((Unit(13), staff.unit(8)), staff, "vib.", font)

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    # WARNING: replace this code with new example provide by neoscore
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 3)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/guitar/gesto8.png',
        wait=True,
        dpi=600)
    UpdateRate(
        8000,
        8,
        f'{home}/guitar/guitar.json',
        gestProb=0.6,
        gestRepetition=1,
        frequencyTarget=pitchHz,
        tupletDuration=889)
    pd_print('GUITAR_gesto8: Rendered!')
    return "Gesto 8 Rendered!"

# ============================================


def GUITAR_gesto9():
    pd_print('GUITAR_gesto9')
    home = getHOME_PATH()
    pitches = get_GUITAR_global_notes()
    amps = get_GUITAR_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 4000, 7600)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 4000, 7600)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 2)
    while True:
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
    midicent = approx_mc(f2mc(pitchHz))
    while True:
        if midicent > 7600:
            midicent = midicent - 1200
        elif midicent < 4000:
            midicent = midicent + 1200
        else:
            break
    midicent = approx_mc(midicent)
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = GUITAR_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    guitarClef = 'treble_8vb'
    Clef(ZERO, staff, guitarClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=False)
    Text((Unit(17), staff.unit(-6)), staff, "tremolo", font)
    font = Font("Arial", Unit(9), italic=True)
    Text((Unit(50), staff.unit(-6)), staff, "(p i m)", font)
    MusicText((Unit(200), staff.unit(-6.5)), staff, "breathMarkComma", scale=0.8)

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    # WARNING: replace this code with new example provide by neoscore
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 3)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/guitar/gesto9.png',
        wait=True,
        dpi=600)
    UpdateRate(
        12000,
        9,
        f'{home}/guitar/guitar.json',
        frequencyTarget=pitchHz,
        tupletDuration=1333)
    pd_print('GUITAR_gesto9: Rendered!')
    return "Gesto 9 Rendered!"

# ============================================


def GUITAR_gesto10():
    pd_print('GUITAR_gesto10')
    home = getHOME_PATH()
    pitches = get_GUITAR_global_notes()
    amps = get_GUITAR_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 4000, 7600)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 4000, 7600)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    spacoBetweenNotes = 20
    numberOfNotes = random.randint(2, 4)
    if numberOfNotes == 3:
        spacoBetweenNotes = 25
    elif numberOfNotes == 2:
        spacoBetweenNotes = 35
    elif numberOfNotes == 4:
        spacoBetweenNotes = 20
    spaco = 5
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    guitarClef = 'treble_8vb'
    Clef(ZERO, staff, guitarClef)

    for x in range(numberOfNotes):
        index = random.randint(1, 3)
        while True:
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
        midicent = approx_mc(f2mc(pitchHz))
        while True:
            if midicent > 6000:
                midicent = midicent - 1200
            elif midicent < 4000:
                midicent = midicent + 1200
            else:
                break
        midicent = midicent
        pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
        alterations = GUITAR_8thTones(midi_alterations)
        octave = get_octave(midicent)
        pitch_info = [(pitch, alterations, octave)]
        Chordrest(Mm(spaco), staff, pitch_info, (int(1), int(1)))
        spaco = spaco + spacoBetweenNotes



    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(15), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(40), staff.unit(-6.5)), staff, "tremolo3", scale=0.8)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicPP", scale=0.8)
    MusicText((Unit(70), staff.unit(-6.3)), staff,
              "dynamicPPP", scale=0.8)
    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    # WARNING: replace this code with new example provide by neoscore
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 3)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    neoscore.render_image(
        rect=None,
        dest=f'{home}/guitar/gesto10.png',
        wait=True,
        dpi=600)
    UpdateRate(
        31000,
        10,
        f'{home}/guitar/guitar.json',
        tupletDuration=2066)
    pd_print('GUITAR_gesto10: Rendered!')
    return "Gesto 10 Rendered!"

# ============================================


def GUITAR_gesto11():
    pd_print('GUITAR_gesto11')
    home = getHOME_PATH()
    pitches = get_GUITAR_global_notes()
    amps = get_GUITAR_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 4000, 7600)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 4000, 7600)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 2)
    while True:
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
    midicent = approx_mc(f2mc(pitchHz))
    while True:
        if midicent > 7600:
            midicent = midicent - 1200
        elif midicent < 4000:
            midicent = midicent + 1200
        else:
            break
    midicent = approx_mc(midicent)
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = GUITAR_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    guitarClef = 'treble_8vb'
    Clef(ZERO, staff, guitarClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(15), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(40), staff.unit(-6.5)), staff, "tremolo3", scale=0.8)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicMP", scale=0.8)
    MusicText((Unit(70), staff.unit(-6.3)), staff,
              "dynamicSforzatoFF", scale=0.8)
    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    # WARNING: replace this code with new example provide by neoscore
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 3)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/guitar/gesto11.png',
        wait=True,
        dpi=600)
    UpdateRate(
        23000,
        11,
        f'{home}/guitar/guitar.json',
        tupletDuration=2300,
        gestProb=0.30,
        gestRepetition=1)
    pd_print('GUITAR_gesto11: Rendered!')
    return "Gesto 11 Rendered!"

# ============================================


def GUITAR_gesto12():
    pd_print('GUITAR_gesto12')
    home = getHOME_PATH()
    pitches = get_GUITAR_global_notes()
    amps = get_GUITAR_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 4000, 7600)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 4000, 7600)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 2)
    while True:
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
    midicent = approx_mc(f2mc(pitchHz))
    while True:
        if midicent > 7600:
            midicent = midicent - 1200
        elif midicent < 4000:
            midicent = midicent + 1200
        else:
            break
    midicent = approx_mc(midicent)
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = GUITAR_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    guitarClef = 'treble_8vb'
    Clef(ZERO, staff, guitarClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    # TODO: colocar s.p. na Bula
    Text((Unit(40), staff.unit(-6)), staff, "diminuindo a cada repetição", font)

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    # WARNING: replace this code with new example provide by neoscore
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")
    note = [('a', '', 3)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    note = [('c', '', 4)]
    Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/guitar/gesto12.png',
        wait=True,
        dpi=600)
    UpdateRate(
        8000,
        12,
        f'{home}/guitar/guitar.json',
        tupletDuration=1143)
    pd_print('GUITAR_gesto12: Rendered!')
    return "Gesto 12 Rendered!"
