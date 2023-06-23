import random
from neoscore.core.units import ZERO, Mm
from neoscore.core import neoscore
from neoscore.core.text import Text
from neoscore.western.chordrest import NoteheadTable
from neoscore.western.hairpin import Hairpin
from public.functions.utilities.utilities import *
from om_py import f2mc, mc2f, approx_mc
try:
    import pd
    pd_print = pd.print
except BaseException:
    pd_print = print

FLUTE_NOTES = []
FLUTE_AMP = []


def set_FLUTE_global_notes(nota):
    global FLUTE_NOTES
    if FLUTE_NOTES is []:
        FLUTE_NOTES = [nota]
    else:
        FLUTE_NOTES.append(nota)
    return "Global notes updated!"


def set_FLUTE_global_amps(nota):
    global FLUTE_AMP
    if FLUTE_AMP is []:
        FLUTE_AMP = [nota]
    else:
        FLUTE_AMP.append(nota)
    return "Global notes updated!"


def get_FLUTE_global_notes():
    global FLUTE_NOTES
    if FLUTE_NOTES == [] or FLUTE_NOTES is None:
        # get 20 aleatory notes
        return random.sample(range(100, 1000), 20)
    else:
        return FLUTE_NOTES


def get_FLUTE_global_amps():
    global FLUTE_AMP
    if FLUTE_AMP == [] or FLUTE_AMP is None:
        aleatoric_amps = random.sample(range(10, 200), 20)
        negative_amps = [x * -1 for x in aleatoric_amps]
        return negative_amps
    else:
        return FLUTE_AMP


def clear_FLUTE_global_notes():
    global FLUTE_NOTES
    FLUTE_NOTES = []
    return "Global notes cleared!"


def clear_FLUTE_global_amps():
    global FLUTE_AMP
    FLUTE_AMP = []
    return "Global amps cleared!"

# ========================================
# ========================================
# ========================================


def FLUTE_midialteration2symbol(alteration):
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


# ========================================
# ========================================
# ========================================
def FLUTE_8thTones(alteration):
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
def FLUTE_add_articulation(figure, gesto, staff):  # TODO - remove staff
    GESTOS = {
        'gesto1': ['articStaccatoAbove', 'articAccentStaccatoAbove', 'articTenutoAboveSmall'],
        'gesto2': ['articStaccatoAbove', 'articTenutoAbove'],
        # TODO: Adicionar outras articulacoes
        'gesto3': ['articStaccatoAbove', 'articTenutoAbove'],
    }
    articulations = GESTOS[gesto]
    MusicText(
        figure.extra_attachment_point,
        figure, random.choice(articulations),
        alignment_x=AlignmentX.CENTER,
        alignment_y=AlignmentY.CENTER,)
    return 'Articulation added!'

# ========================================


def FLUTE_add_dynamic(space, staff, gesto):
    DYNAMICS = {
        'gesto1': ['f', 'mf', 'ff'],
        'gesto2': ['p', 'pp', 'fp'],
    }
    dynamic_random = random.choice([True, False])
    if dynamic_random:
        Dynamic((Mm(space), staff.unit(12)), staff,
                random.choice(DYNAMICS[gesto]))

# ========================================


def FLUTE_tremoloPosition(midicent):
    if midicent >= 6500 and midicent < 6700:
        return 4
    elif midicent >= 6700 and midicent < 6900:
        return 4.5
    elif midicent >= 6900 and midicent < 7100:
        return 3.5
    elif midicent >= 7100 and midicent < 7300:
        return 4.5
    elif midicent >= 7300 and midicent < 7500:
        return 3.5
    elif midicent >= 7500 and midicent < 8400:
        return 2.5
    elif midicent >= 8400 and midicent < 9600:
        return 1.5
    else:
        pd_print('Not tremolo position!')
        return 0

# ========================================
# ========================================
# ========================================


def FLUTE_gesto0():
    home = getHOME_PATH()
    default = neoscore.default_font  # Alias just for docs legibility
    sample = "The Score is ready!"
    Text((ZERO, Mm(0)), None, sample, default.modified(size=Unit(29)))
    # UpdateRate(0, 1, "gesto0", f'{home}/flute/flute.json')
    neoscore.render_image(
        rect=None,
        dest=f'{home}/flute/gesto0.png',
        wait=True,
        dpi=600)
    UpdateRate(0, 0, f'{home}/flute/flute.json')
    return "Gesto 0 Rendered!"


# ========================================
# ========================================
# ========================================

def FLUTE_gesto1():
    home = getHOME_PATH()
    pd_print('FLUTE_gesto1')
    # Get Pitches from FFT analisys
    pitches = get_FLUTE_global_notes()
    pitches = PitchesInsideRange(pitches, 7200, 9300)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 7200, 9300)
        pd_print('Choosing aleatory pitches!')
    NOTEHEAD = NoteheadTable(
        "noteheadSquareBlack",
        "noteheadSquareBlack",
        "noteheadSquareBlack",
        "noteheadSquareBlack")  # cabeça de notas
    fixed_gesture_number = random.randint(2, 4)
    # Generate random gestures
    gesture_number = fixed_gesture_number
    score_horizontal_position = 0
    while gesture_number > 0:
        gesture_number -= 1
        Path.rect((Mm(score_horizontal_position), Mm(-14)), None, Mm(80),
                  Mm(30), Brush(Color(255, 255, 255, 255)), Pen(thickness=Mm(0.5)))
        POSITION = (Mm(score_horizontal_position), Mm(0))
        if fixed_gesture_number == 4:
            notes_number = random.randint(2, 4)
        elif fixed_gesture_number == 3:
            notes_number = random.randint(3, 5)
        elif fixed_gesture_number == 2:
            notes_number = random.randint(4, 6)
        fixed_notes_number = notes_number
        staff = Staff(POSITION, None, Mm(80))
        staff.unit(7)
        space = 10
        Clef(ZERO, staff, 'treble')
        number_of_iterations = 0
        while notes_number > 0:
            try:
                midicent = f2mc(random.choice(pitches)) - 1200  # transposition of flautin
            except BaseException:
                pitches = aleatoric_freqs(40, 7400, 9300) - 1200  # transposition of flautin
                midicent = f2mc(random.choice(pitches))
            # took the first two list of one return thing1, thing2, thing3
            pitch, midi_alterations, cents = get_midi_class_of_midicent(
                midicent)
            alterations = FLUTE_midialteration2symbol(midi_alterations)
            if alterations is not None:
                notes_number -= 1
                octave = get_octave(midicent)
                # TODO: Quando a nota anterior for sus ou bemol e a atual for
                # bequadro adicionar bequadro
                note = [(pitch, alterations, octave)]
                tremolo_position = Unit(3)  # NOTE: positivo é pra direita
                note = Chordrest(
                    Mm(space), staff, note, (1, 1), table=NOTEHEAD)
                if random.randint(
                        0, 100) > 80:  # NOTE:  20% de adicionar tremollo
                    staff_unit = FLUTE_tremoloPosition(midicent)
                    tremolo_number = random.randint(3, 5)
                    MusicText((tremolo_position, staff.unit(staff_unit)),
                              note, f"tremolo{tremolo_number}")
                else:
                    FLUTE_add_articulation(note, gesto='gesto1', staff=staff)
                space += (70 / fixed_notes_number) * \
                    (random.randint(70, 110) / 100)
            number_of_iterations += 1
            if number_of_iterations > 100:
                break
        score_horizontal_position += 90
    neoscore.render_image(
        rect=None,
        dest=f'{home}/flute/gesto1.png',
        wait=True)
    UpdateRate(6000, 1, f'{home}/flute/flute.json')
    pd_print('FLUTE_gesto1: Rendered!')
    return "Gesto 1 Rendered!"

# ========================================
# ========================================
# ========================================


def FLUTE_gesto2():
    pd_print('FLUTE_gesto2')
    home = getHOME_PATH()
    pitches = get_FLUTE_global_notes()
    amps = get_FLUTE_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 7400, 9300)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 7400, 9300)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = 7
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
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    staff.unit(7)
    space = 10
    Clef(ZERO, staff, 'treble')
    midicent = f2mc(pitch_8th) - 1200
    midicent = approx_mc(midicent)
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    wait_good_alteration = True
    numberOfIntations = 0
    while wait_good_alteration:
        numberOfIntations += 1
        if numberOfIntations > 100:
            pitch, midi_alterations, cents = get_midi_class_of_midicent(6000)
        alterations = FLUTE_midialteration2symbol(midi_alterations)
        if alterations is not None:
            octave = get_octave(midicent)
            # TODO: Quando a nota anterior for sus ou bemol e a atual for
            # bequadro adicionar bequadro
            pitch_info = [(pitch, alterations, octave)]
            note = Chordrest(Mm(space), staff, pitch_info, (int(1), int(1)))
            Hairpin((ZERO, staff.unit(6)), note, (staff.unit(35), ZERO))
            POSITION = Unit(29)
            Dynamic((POSITION, staff.unit(10)), staff, "p")
            POSITION = Unit(200)
            Dynamic((POSITION, staff.unit(10)), staff, "ffff")
            wait_good_alteration = False

    # just show image, without page
    neoscore.render_image(
        rect=None,
        dest=f'{home}/flute/gesto2.png',
        wait=True,
        dpi=900)
    UpdateRate(3000, 2, f'{home}/flute/flute.json')
    pd_print('FLUTE_gesto2: Rendered!')
    return "Gesto 2 Rendered!"

# ================================================================
# ================== TERCEIRO MOVIMENTO ==========================
# ================================================================


def FLUTE_gesto3():
    pd_print('FLUTE_gesto3')
    home = getHOME_PATH()
    pitches = get_FLUTE_global_notes()
    amps = get_FLUTE_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 5900, 7200)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 7200, 9300)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = 2  # NOTE: Here we choose the second pitch more loud
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = 6100
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
            midicent = 6200

        if midicent > 8200:
            midicent = midicent - 1200
        elif midicent < 6000:
            midicent = midicent + 1200
        else:
            break
    pitchHz = mc2f 
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = FLUTE_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]

    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    Clef(ZERO, staff, 'treble')
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(18), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(27), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    Text((Unit(20), staff.unit(-6)), staff, "sing.", font)
    Text((Unit(45), staff.unit(-6)), staff, "ord.", font)


    MusicText((Unit(80), staff.unit(-6.3)), staff, "dynamicFF", scale=0.8)
    MusicText((Unit(95), staff.unit(-6.3)), staff,
              "dynamicPP", scale=0.8)

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
    # Fim desenhar chave de repetição

    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/flute/gesto3.png',
        wait=True,
        dpi=600)
    UpdateRate(
        15000,
        3,
        f'{home}/flute/flute.json',
        # frequencyTarget=pitchHz,
        tupletDuration=1000)
    pd_print('FLUTE_gesto3: Rendered!')
    return "Gesto 3 Rendered!"

# ================================================================


def FLUTE_gesto4():
    pd_print('FLUTE_gesto4')
    home = getHOME_PATH()
    pitches = get_FLUTE_global_notes()
    amps = get_FLUTE_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 5900, 7200)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 7200, 9300)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(6100)
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
            midicent = 6100
            break

        if midicent > 8200:
            midicent = midicent - 1200
        elif midicent < 6000:
            midicent = midicent + 1200
        else:
            break

    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = FLUTE_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    Clef(ZERO, staff, 'treble')
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(40), staff.unit(-6.5)), staff, "tremolo3", scale=0.8)

    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicPP", scale=0.8)
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
        dest=f'{home}/flute/gesto4.png',
        wait=True,
        dpi=600)
    UpdateRate(
        17000,
        4,
        f'{home}/flute/flute.json',
        frequencyTarget=pitchHz,
        tupletDuration=1307)  # NOTE: 13:17
    pd_print('FLUTE_gesto4: Rendered!')
    return "Gesto 4 Rendered!"


# ============================================
def FLUTE_gesto5():
    pd_print('FLUTE_gesto5')
    home = getHOME_PATH()
    pitches = get_FLUTE_global_notes()
    amps = get_FLUTE_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        # if C3 is 4800 Eb2 is 3900
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
            pitch_8th = mc2f(7900)

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
    iteration = 0
    while True:
        iteration += 1
        if iteration > 25:
            midicent = 7900
            break

        if midicent > 8200:
            midicent = midicent - 1200
        elif midicent < 6000:
            midicent = midicent + 1200
        else:
            break
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = FLUTE_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble'
    Clef(ZERO, staff, saxClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-13)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-5.5)), staff, "ord.", font)
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
        dest=f'{home}/flute/gesto5.png',
        wait=True,
        dpi=600)
    UpdateRate(
        22000,
        5,
        f'{home}/flute/flute.json',
        frequencyTarget=pitchHz,
        tupletDuration=1466,
        startPlay=0,
        gestRepetition=1, 
        gestProb=0.45)
    pd_print('FLUTE_gesto5: Rendered!')
    return "Gesto 5 Rendered!"

# ============================================


def FLUTE_gesto6():
    pd_print('FLUTE_gesto6')
    home = getHOME_PATH()
    pitches = get_FLUTE_global_notes()
    amps = get_FLUTE_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 6000, 8400)
    if pitches is None or pitches is []:
        # if C3 is 4800 Eb2 is 3900
        pitches = aleatoric_freqs(40, 6000, 8400)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    iteration = 0
    while True:
        iteration += 1
        if iteration > 25:
            pitch_8th = mc2f(6300)
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
    iteration = 0
    while True:
        iteration += 1
        if midicent > 8200:
            midicent = midicent - 1200
        elif midicent < 6000:
            midicent = midicent + 1200
        else:
            break

        if iteration > 25:
            midicent = 6300
            break
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = FLUTE_8thTones(midi_alterations)
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
     # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "ord.", font)
    MusicText((Unit(40), staff.unit(-6.5)), staff, "tremolo3", scale=0.8)
    
    MusicText((Unit(70), staff.unit(-6.3)), staff,
              "dynamicFortePiano", scale=0.8)

    MusicText((Unit(60), staff.unit(-6.3)), staff,
              "dynamicPiano", scale=0.8)

    neoscore.render_image(
        rect=None,
        dest=f'{home}/flute/gesto6.png',
        wait=True,
        dpi=600)
    UpdateRate(
        7000,
        6,
        f'{home}/flute/flute.json',
        frequencyTarget=pitchHz,
        tupletDuration=1166,
        startPlay=0,
        gestProb=0.5,
        gestRepetition=1)
    pd_print('FLUTE_gesto6: Rendered!')
    return "Gesto 6 Rendered!"

# ============================================


def FLUTE_gesto7():
    home = getHOME_PATH()
    pitches = get_FLUTE_global_notes()
    amps = get_FLUTE_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        # if C3 is 4800 Eb2 is 3900
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
            pitch_8th = mc2f(6100)
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
    iteration = 0
    while True:
        iteration += 1
        if iteration > 25:
            midicent = 6400
            break

        if midicent > 8200:
            midicent = midicent - 1200
        elif midicent < 6000:
            midicent = midicent + 1200
        else:
            break
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = FLUTE_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble'
    Clef(ZERO, staff, saxClef)
    # Articulações

    # Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
    #           Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    MusicText((Unit(20), staff.unit(-4)), staff,
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
        dest=f'{home}/flute/gesto7.png',
        wait=True,
        dpi=600)
    UpdateRate(
        8000,
        7,
        f'{home}/flute/flute.json',
        frequencyTarget=pitchHz,
        tupletDuration=1000)
    pd_print('FLUTE_gesto7: Rendered!')
    return "Gesto 7 Rendered!"

# ============================================


def FLUTE_gesto8():
    pd_print('FLUTE_gesto8')
    home = getHOME_PATH()
    pitches = get_FLUTE_global_notes()
    amps = get_FLUTE_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        # if C3 is 4800 Eb2 is 3900
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
            pitch_8th = mc2f(7300)
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
    iteration = 0
    while True:
        iteration += 1 
        if midicent > 7201:
            midicent = midicent - 1200
        elif midicent < 5950:
            midicent = midicent + 1200
        else:
            break
        if iteration > 25:
            midicent = 6700
            break
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = FLUTE_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble'
    Clef(ZERO, staff, saxClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    # TODO: colocar s.p. na Bula

    Text((Unit(14), staff.unit(-2)), staff, "aeolian", font)
    noteheads = NoteheadTable(
        "noteheadCircleXWhole",
        "noteheadCircleXWhole",
        "noteheadCircleXWhole",
        "noteheadCircleXWhole")

    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)), table=noteheads)


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
   
    neoscore.render_image(
        rect=None,
        dest=f'{home}/flute/gesto8.png',
        wait=True,
        dpi=600)
    UpdateRate(
        11000,
        8,
        f'{home}/flute/flute.json',
        frequencyTarget=pitchHz,
        tupletDuration=917,
        gestRepetition=1, 
        gestProb=0.30)
    pd_print('FLUTE_gesto8: Rendered!')
    return "Gesto 8 Rendered!"

# ============================================


def FLUTE_gesto9():
    pd_print('FLUTE_gesto9')
    home = getHOME_PATH()
    pitches = get_FLUTE_global_notes()
    amps = get_FLUTE_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        # if C3 is 4800 Eb2 is 3900
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
            pitch_8th = mc2f(7850)
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
    iteration = 0
    while True:
        iteration += 1
        if midicent > 8200:
            midicent = midicent - 1200
        elif midicent < 6000:
            midicent = midicent + 1200
        else:
            break
        if iteration > 50:
            midicent = 6753
            break

    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = FLUTE_8thTones(midi_alterations)
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
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicPP", scale=0.8)
    MusicText((Unit(70), staff.unit(-6.3)), staff,
              "dynamicMP", scale=0.8)

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
        dest=f'{home}/flute/gesto9.png',
        wait=True,
        dpi=600)
    UpdateRate(
        23000,
        9,
        f'{home}/flute/flute.json',
        frequencyTarget=pitchHz,
        tupletDuration=1278, 
        gestRepetition=1, 
        gestProb=0.10)
    pd_print('FLUTE_gesto9: Rendered!')
    return "Gesto 9 Rendered!"

# ============================================


def FLUTE_gesto10():
    pd_print('FLUTE_gesto10')
    home = getHOME_PATH()
    pitches = get_FLUTE_global_notes()
    amps = get_FLUTE_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        # if C3 is 4800 Eb2 is 3900
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
            pitch_8th = mc2f(6600)
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
    iteration = 0
    while True:
        iteration += 1
        if midicent > 8200:
            midicent = midicent - 1200
        elif midicent < 6000:
            midicent = midicent + 1200
        else:
            break
        if iteration > 50:
            midicent = 6753

        pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = FLUTE_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    saxClef = 'treble'
    Clef(ZERO, staff, saxClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    # TODO: colocar s.p. na Bula

    Text((Unit(14), staff.unit(-2)), staff, "aeolian", font)
    noteheads = NoteheadTable(
        "noteheadCircleXWhole",
        "noteheadCircleXWhole",
        "noteheadCircleXWhole",
        "noteheadCircleXWhole")

    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)), table=noteheads)


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

    neoscore.render_image(
        rect=None,
        dest=f'{home}/flute/gesto10.png',
        wait=True,
        dpi=600)
    UpdateRate(
        12000,
        10,
        f'{home}/flute/flute.json',
        frequencyTarget=pitchHz,
        tupletDuration=1000)
    pd_print('FLUTE_gesto10: Rendered!')
    return "Gesto 10 Rendered!"

# ============================================


def FLUTE_gesto11():
    pd_print('FLUTE_gesto11')
    home = getHOME_PATH()
    pitches = get_FLUTE_global_notes()
    amps = get_FLUTE_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        # if C3 is 4800 Eb2 is 3900
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
            pitch_8th = mc2f(6560)
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
        pd.print(iterations)
        if iterations > 25:
            midicent = 7400
            break
        if midicent > 7300:
            midicent = midicent - 1200
        elif midicent < 6000:
            midicent = midicent + 1200
        else:
            break
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = FLUTE_8thTones(midi_alterations)
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
    MusicText((Unit(73), staff.unit(-6.3)), staff,
              "dynamicFF", scale=0.8)

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
        dest=f'{home}/flute/gesto11.png',
        wait=True,
        dpi=600)
    UpdateRate(
        31000,
        11,
        f'{home}/flute/flute.json',
        frequencyTarget=pitchHz,
        tupletDuration=1632, 
        gestRepetition=1, 
        gestProb=0.30)
    pd_print('FLUTE_gesto11: Rendered!')
    return "Gesto 11 Rendered!"

# ============================================


def FLUTE_gesto12():
    pd_print('FLUTE_gesto12')
    home = getHOME_PATH()
    pitches = get_FLUTE_global_notes()
    amps = get_FLUTE_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3900, 6000)
    if pitches is None or pitches is []:
        # if C3 is 4800 Eb2 is 3900
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
            pitch_8th = mc2f(6800)
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
            midicent = 6800
            break
        if midicent > 8200:
            midicent = midicent - 1200
        elif midicent < 6000:
            midicent = midicent + 1200
        else:
            break
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = FLUTE_8thTones(midi_alterations)
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
        dest=f'{home}/flute/gesto12.png',
        wait=True,
        dpi=600)
    UpdateRate(
        13000,
        12,
        f'{home}/flute/flute.json',
        frequencyTarget=pitchHz,
        tupletDuration=2000)
    pd_print('FLUTE_gesto11: Rendered!')
    return "Gesto 11 Rendered!"
