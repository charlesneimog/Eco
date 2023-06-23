import random
from neoscore.core.units import ZERO, Mm, Unit
from neoscore.core import neoscore
from neoscore.core.text import Text
from neoscore.western.chordrest import NoteheadTable
from public.functions.utilities.utilities import *
from om_py import f2mc, mc2f, approx_mc
try:
    import pd
    pd_print = pd.print
except BaseException:
    pd_print = print


CELLO_NOTES = []
CELLO_AMPS = []


def set_CELLO_global_notes(nota):
    global CELLO_NOTES
    if CELLO_NOTES is None:
        CELLO_NOTES = [nota]
    else:
        CELLO_NOTES.append(nota)
    return "Global notes updated!"


def set_CELLO_global_amps(amp):
    global CELLO_AMPS
    if CELLO_AMPS is None:
        CELLO_AMPS = [amp]
    else:
        CELLO_AMPS.append(amp)
    return "Global amp updated!"


def get_CELLO_global_notes():
    global CELLO_NOTES
    if CELLO_NOTES == [] or CELLO_NOTES is None:
        # get 20 aleatory notes
        return random.sample(range(100, 1000), 20)
    else:
        return CELLO_NOTES


def get_CELLO_global_amps():
    global CELLO_AMPS
    if CELLO_AMPS == [] or CELLO_AMPS is None:
        aleatoric_amps = random.sample(range(10, 200), 20)
        negative_amps = [x * -1 for x in aleatoric_amps]
        return negative_amps
    else:
        return CELLO_AMPS


def clear_CELLO_global_notes():
    global CELLO_NOTES
    CELLO_NOTES = []
    return "Global notes cleared!"


def clear_CELLO_global_amps():
    global CELLO_AMPS
    CELLO_AMPS = []
    return "Global amp cleared!"

# ========================================


def CELLO_midialteration2symbol(alteration):
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


def CELLO_add_articulation(figure, gesto, staff):  # TODO: remove staffs
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


def CELLO_tremoloPosition(midicent):  # TODO: remove octavte from all functions
    if midicent < 6850:
        return 6
    elif midicent >= 7100 and midicent < 7300:
        return 4.5
    elif midicent >= 7300 and midicent < 7500:
        return 5
    elif midicent >= 7500 and midicent < 8400:
        return 2.5
    elif midicent >= 8400 and midicent < 9600:
        return 1.5
    else:
        return 0


def CELLO_8thTones(alteration):
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


def gestError(Instrument, gestName, errorName):
    HOME = getHOME_PATH()
    nameFile = f'{HOME}/{Instrument}/{gestName}.txt'
    # if file already exist, append
    if os.path.isfile(nameFile):
        with open(nameFile, 'a') as f:
            f.write(f'{errorName} \n')
    else:
        # create file and write
        with open(nameFile, 'w') as f:
            f.write(f'{errorName} \n')
    return None


# ========================================
# ========================================
# ========================================
def CELLO_gesto0():
    HOME = getHOME_PATH()
    default = neoscore.default_font  # Alias just for docs legibility
    sample = " The Score Player is ready! "
    Text((ZERO, Mm(180)), None, sample, default.modified(size=Unit(30)))
    # UpdateRate(measureDuration, gestureNumber, filePathname,
    # frequencyTarget=0, tupletDuration=0, startPlay=0):
    UpdateRate(0, 0, f'{HOME}/cello/cello.json')
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/cello/gesto0.png',
        wait=True,
        dpi=900)
    return "Gesto 0 Rendered!"

# ========================================


def CELLO_gesto1():
    pd_print('CELLO_gesto1')
    HOME = getHOME_PATH()
    cello_pitches = get_CELLO_global_notes()
    cello_pitches = FreqsInsideRange(cello_pitches, 6000, 7900)
    if cello_pitches is None or cello_pitches == []:
        # aleatoric freqs return a list of freqs in Hz
        cello_pitches = aleatoric_freqs(40, 6000, 7900)
        gestError('cello', 'gesto1', 'Choosing aleatory pitches')
    score_horizontal_position = 0
    space = 10

    # WHITE RECTANGLE
    score_horizontal_position = 0
    Path.rect((Mm(score_horizontal_position), Mm(-12)), None, Mm(80),
              Mm(30), Brush(Color(255, 255, 255, 255)), Pen(thickness=Mm(-1)))
    POSITION = (Mm(score_horizontal_position + 2), Mm(0))

    # WHITE RECTANGLE
    fixed_notes_number = random.randint(3, 5)
    notes_number = fixed_notes_number
    score_horizontal_position = 90
    Path.rect((Mm(score_horizontal_position), Mm(-12)), None, Mm(80),
              Mm(30), Brush(Color(255, 255, 255, 255)), Pen(thickness=Mm(0.5)))
    POSITION = (Mm(score_horizontal_position + 2), Mm(0))
    staff = Staff(POSITION, None, Mm(78))
    staff.unit(7)
    space = 10
    Clef(ZERO, staff, 'treble')
    number_of_iterations = 0
    sulpont = (Mm(score_horizontal_position + 3), Mm(-4))
    Text(
        sulpont,
        None,
        'sul pont.',
        neoscore.default_font.modified(
            size=Unit(10),
            italic=True))
    noteheads = NoteheadTable(
        "noteheadBlack",
        "noteheadBlack",
        "noteheadBlack",
        "noteheadBlack")
    while notes_number > 0:
        choosed_freq = random.choice(cello_pitches)
        midicent = f2mc(choosed_freq)
        iterationNew = 0
        while True:
            iterationNew += 1
            if iterationNew > 50:
                midicent = 6400
                break
            if midicent > 6900:
                midicent = midicent - 1200
            elif midicent < 5500:
                midicent = midicent + 1200
            else:
                break
        choosed_freq = mc2f(midicent)
        pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
        alterations = CELLO_midialteration2symbol(midi_alterations)
        if alterations is not None:
            octave = get_octave(midicent)
            note = [(pitch, alterations, octave)]
            tremolo_position = Unit(3)  # positivo é pra diretira
            note = Chordrest(Mm(space), staff, note,
                             (int(1), int(1)), table=noteheads)
            space += (70 / fixed_notes_number) * \
                (random.randint(70, 110) / 100)
            staff_unit = CELLO_tremoloPosition(midicent)
            MusicText((tremolo_position, staff.unit(
                staff_unit)), note, f"tremolo3")
            notes_number -= 1
        number_of_iterations += 1
        if number_of_iterations > 100:
            gestError('cello', 'gesto1', 'Too many iterations!')
            break
    score_horizontal_position = 0 + 180
    Path.rect((Mm(score_horizontal_position), Mm(-12)), None, Mm(80),
              Mm(30), Brush(Color(255, 255, 255, 255)), Pen(thickness=Mm(-1)))
    POSITION = (Mm(score_horizontal_position + 2), Mm(0))
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/cello/gesto1.png',
        wait=True)
    UpdateRate(6000, 1, f'{HOME}/cello/cello.json')
    return "Gesto 1 Rendered!"


def CELLO_gesto2():
    pd_print('CELLO_gesto2')
    HOME = getHOME_PATH()
    PITCHES = get_CELLO_global_notes()
    AMPS = get_CELLO_global_amps()
    PITCHES, AMPS = FreqsAndAmps_InsideRange(PITCHES, AMPS, 6000, 7500)
    gestError('cello', 'gesto2', str(PITCHES))
    gestError('cello', 'gesto2', str(AMPS))
    if PITCHES is None or PITCHES is []:
        PITCHES = aleatoric_freqs(40, 6000, 7500)
        gestError('cello', 'gesto2', 'no Good pitches founded')
        AMPS = random.sample(range(-10, -200), 40)
    if len(PITCHES) != len(AMPS):
        gestError(
            'cello',
            'gesto2',
            'number of pitches and AMPS are different')
        return None
    # sort amps ascending
    sorted_amp = sorted(AMPS, reverse=True)
    index = 7
    while True:
        try:
            sorted_amp = sorted(AMPS, reverse=True)
            amp_8th = sorted_amp[index]
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
    midicent = f2mc(pitch_8th)
    midicent = approx_mc(midicent)
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    wait_good_alteration = True
    numberOfIntations = 0
    while wait_good_alteration:
        alterations = CELLO_midialteration2symbol(midi_alterations)
        if numberOfIntations > 100:
            pitch, midi_alterations, cents = get_midi_class_of_midicent(6000)
        if alterations is not None:
            octave = get_octave(midicent)
            note = [(pitch, alterations, octave)]  # TODO: Add alterations
            tremolo_position = Unit(3)  # positivo é pra diretira
            note = Chordrest(Mm(space), staff, note, (int(1), int(1)))
            Hairpin((ZERO, staff.unit(6)), note, (staff.unit(35), ZERO))
            POSITION = Unit(29)
            Dynamic((POSITION, staff.unit(10)), staff, "p")
            POSITION = Unit(200)
            Dynamic((POSITION, staff.unit(10)), staff, "ffff")
            wait_good_alteration = False
    # just show image, without page
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/cello/gesto2.png',
        wait=True,
        dpi=600)
    UpdateRate(3000, 2, f'{HOME}/cello/cello.json')
    pd_print('CELLO_gesto2: Rendered!')
    return "Gesto 2 Rendered!"


# ===================================================

def CELLO_gesto3():
    pd_print("CELLO_gesto3")  # PAUSA:
    HOME = getHOME_PATH()
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    staff.unit(7)
    Chordrest(Mm(35), staff, None, (1, 1))
    Clef(ZERO, staff, 'treble')
    neoscore.render_image(
        rect=None,
        dest=f'{HOME}/cello/gesto3.png',
        wait=True,
        dpi=300)
    UpdateRate(15000, 3, f'{HOME}/cello/cello.json')
    pd_print("CELLO_gesto3 - Gesto 3 Rendered!")
    return "Gesto 3 Rendered!"


def CELLO_gesto4():
    pd_print('CELLO_gesto4')
    home = getHOME_PATH()
    pitches = get_CELLO_global_notes()
    amps = get_CELLO_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3600, 7200)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3600, 7200)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
        gestError('cello', 'gesto4', 'no Good pitches founded')
    if len(pitches) != len(amps):
        gestError(
            'cello',
            'gesto4',
            'number of pitches and AMPS are different')
        return None
    index = random.randint(1, 5)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(4500)
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
        if midicent > 7200:
            midicent = midicent - 1200
        elif midicent < 3600:
            midicent = midicent + 1200
        else:
            break

        if iteration > 50:
            midicent = 6000
            break
    pitchHz = mc2f(midicent)
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = CELLO_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    if midicent > 6200:
        celloClef = 'treble'
    else:
        celloClef = 'bass'

    Clef(ZERO, staff, celloClef)
    font = Font("Arial", Unit(9), italic=True)
    # NOTE: rect(HORIZONTAL, VERTICAL

    # TODO: colocar s.p. na Bula
    Text((Unit(15), staff.unit(-4)), staff, "flautato", font)
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")

    if celloClef == 'treble':
        note = [('a', '', 4)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('c', '', 5)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    else:
        note = [('c', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('e', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)

    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/cello/gesto4.png',
        wait=True,
        dpi=600)
    UpdateRate(
        17000,
        4,
        f'{home}/cello/cello.json',
        frequencyTarget=pitchHz,
        tupletDuration=809)  # NOTE: 21:17
    pd_print('CELLO_gesto4: Rendered!')
    return "Gesto 4 Rendered!"

# ===================================================


def CELLO_gesto5():
    pd_print("CELLO_gesto5")  # PAUSA:
    home = getHOME_PATH()
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    staff.unit(7)
    Chordrest(Mm(35), staff, None, (1, 1))
    Clef(ZERO, staff, 'treble')
    neoscore.render_image(
        rect=None,
        dest=f'{home}/cello/gesto5.png',
        wait=True,
        dpi=300)
    UpdateRate(22000, 5, f'{home}/cello/cello.json')
    pd_print("CELLO_gesto5 - Gesto 5 Rendered!")
    return "Gesto 5 Rendered!"

# ===================================================


def CELLO_gesto6():
    pd_print('CELLO_gesto6')
    home = getHOME_PATH()
    pitches = get_CELLO_global_notes()
    amps = get_CELLO_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3600, 7200)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3600, 7200)
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
            midicent = 5500
            break
        if midicent > 7200:
            midicent = midicent - 1200
        elif midicent < 3600:
            midicent = midicent + 1200
        else:
            break
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = CELLO_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    staff_unit = CELLO_tremoloPosition(midicent)
    if midicent > 6200:
        celloClef = 'treble'
    else:
        celloClef = 'bass'

    Clef(ZERO, staff, celloClef)
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(18), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(25), Mm(-14)), None, Mm(25), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "pizz.", font)
    Text((Unit(45), staff.unit(-6)), staff, "arco", font)


    Text((Unit(75), staff.unit(-6)), staff, "cresc.", font)
    Text((Unit(105), staff.unit(-6)), staff, "dim.", font)

    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")

    if celloClef == 'treble':
        note = [('a', '', 4)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('c', '', 5)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    else:
        note = [('c', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('e', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)

    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/cello/gesto6.png',
        wait=True,
        dpi=600)
    UpdateRate(
        8000,
        6,
        f'{home}/cello/cello.json',
        frequencyTarget=pitchHz,
        tupletDuration=1143)  # NOTE: 21:17
    pd_print('CELLO_gesto6: Rendered!')
    return "Gesto 6 Rendered!"

# ===================================================


def CELLO_gesto7():
    pd_print('CELLO_gesto7')
    home = getHOME_PATH()
    pitches = get_CELLO_global_notes()
    amps = get_CELLO_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3600, 7200)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3600, 7200)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(5900)
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
            pitch_8th = mc2f(5900)
            break
        if midicent > 7200:
            midicent = midicent - 1200
        elif midicent < 3600:
            midicent = midicent + 1200
        else:
            break
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = CELLO_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    if midicent > 6200:
        celloClef = 'treble'
    else:
        celloClef = 'bass'

    Clef(ZERO, staff, celloClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "s.p.", font)
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

    if celloClef == 'treble':
        note = [('a', '', 4)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('c', '', 5)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    else:
        note = [('c', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('e', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)

    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/cello/gesto7.png',
        wait=True,
        dpi=600)
    UpdateRate(
        11000,
        7,
        f'{home}/cello/cello.json',
        frequencyTarget=pitchHz,
        tupletDuration=1833)  # NOTE: 21:17
    pd_print('CELLO_gesto7: Rendered!')
    return "Gesto 7 Rendered!"

# ===================================================


def CELLO_gesto8():
    pd_print('CELLO_gesto8')
    home = getHOME_PATH()
    pitches = get_CELLO_global_notes()
    amps = get_CELLO_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3600, 7200)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3600, 7200)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(5000)
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
            midicent = 5000
            break
        if midicent > 4801:
            midicent = midicent - 1200
        elif midicent < 3600:
            midicent = midicent + 1200
        else:
            break
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = CELLO_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    if midicent > 6200:
        celloClef = 'treble'
    else:
        celloClef = 'bass'

    Clef(ZERO, staff, celloClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(17), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(25), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "molto s.p.", font)
    MusicText((Unit(75), staff.unit(-6.3)), staff, "dynamicPPP", scale=0.8)

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")

    if celloClef == 'treble':
        note = [('a', '', 4)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('c', '', 5)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    else:
        note = [('c', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('e', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)

    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/cello/gesto8.png',
        wait=True,
        dpi=600)
    UpdateRate(
        13000,
        8,
        f'{home}/cello/cello.json',
        frequencyTarget=pitchHz,
        tupletDuration=867)  # NOTE: 21:17
    pd_print('CELLO_gesto8: Rendered!')
    return "Gesto 8 Rendered!"

# ===================================================


def CELLO_gesto9():
    pd_print('CELLO_gesto9')
    home = getHOME_PATH()
    pitches = get_CELLO_global_notes()
    amps = get_CELLO_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3600, 7200)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3600, 7200)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(6700)
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
            midicent = 6700
            break
        print("Inside Whilte:", midicent)
        if midicent > 7200:
            midicent = midicent - 1200
        elif midicent < 3600:
            midicent = midicent + 1200
        else:
            break
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = CELLO_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    if midicent > 6200:
        celloClef = 'treble'
    else:
        celloClef = 'bass'

    Clef(ZERO, staff, celloClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(18), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "s.t.", font)
    MusicText((Unit(55), staff.unit(-6.3)), staff, "dynamicMP", scale=0.8)
    MusicText((Unit(75), staff.unit(-6.3)), staff, "dynamicForte", scale=0.8)

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")

    if celloClef == 'treble':
        note = [('a', '', 4)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('c', '', 5)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    else:
        note = [('c', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('e', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)

    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/cello/gesto9.png',
        wait=True,
        dpi=600)
    UpdateRate(
        31000,
        9,
        f'{home}/cello/cello.json',
        frequencyTarget=pitchHz,
        tupletDuration=1530)  # NOTE: 21:17
    pd_print('CELLO_gesto9: Rendered!')
    return "Gesto 9 Rendered!"

# ===================================================


def CELLO_gesto10():
    pd_print('CELLO_gesto10')
    home = getHOME_PATH()
    pitches = get_CELLO_global_notes()
    amps = get_CELLO_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3600, 7200)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3600, 7200)
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
        if midicent > 7200:
            midicent = midicent - 1200
        elif midicent < 3600:
            midicent = midicent + 1200
        else:
            break
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = CELLO_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    if midicent > 6200:
        celloClef = 'treble'
    else:
        celloClef = 'bass'

    Clef(ZERO, staff, celloClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    Path.rect((Mm(5), Mm(-14)), None, Mm(14), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects
    Path.rect((Mm(20), Mm(-14)), None, Mm(12), Mm(5),
              Brush.no_brush(), Pen(thickness=Mm(0.25)))  # rects

    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "flautato", font)
    MusicText((Unit(60), staff.unit(-6.3)), staff, "dynamicPP", scale=0.8)
    MusicText((Unit(75), staff.unit(-6.3)), staff,
                "dynamicMP", scale=0.8)
    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")

    if celloClef == 'treble':
        note = [('a', '', 4)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('c', '', 5)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    else:
        note = [('c', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('e', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)

    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/cello/gesto10.png',
        wait=True,
        dpi=600)
    UpdateRate(
        23000,
        10,
        f'{home}/cello/cello.json',
        frequencyTarget=pitchHz,
        tupletDuration=1643)  # NOTE: 21:17
    pd_print('CELLO_gesto10: Rendered!')
    return "Gesto 10 Rendered!"

# ===================================================


def CELLO_gesto11():
    pd_print('CELLO_gesto11')
    home = getHOME_PATH()
    pitches = get_CELLO_global_notes()
    amps = get_CELLO_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3600, 7200)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3600, 7200)
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
        if midicent > 7200:
            midicent = midicent - 1200
        elif midicent < 3600:
            midicent = midicent + 1200
        else:
            break
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = CELLO_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    if midicent > 6200:
        celloClef = 'treble'
    else:
        celloClef = 'bass'

    Clef(ZERO, staff, celloClef)
    # Articulações
    # TODO: colocar s.p. na Bula

    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")

    if celloClef == 'treble':
        note = [('a', '', 4)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('c', '', 5)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    else:
        note = [('c', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('e', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)

    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/cello/gesto11.png',
        wait=True,
        dpi=600)
    UpdateRate(
        12000,
        11,
        f'{home}/cello/cello.json',
        frequencyTarget=pitchHz,
        tupletDuration=1714)  # NOTE: 21:17
    pd_print('CELLO_gesto11: Rendered!')
    return "Gesto 11 Rendered!"

# ===================================================


def CELLO_gesto12():
    home = getHOME_PATH()
    pitches = get_CELLO_global_notes()
    amps = get_CELLO_global_amps()
    pitches, amps = FreqsAndAmps_InsideRange(pitches, amps, 3600, 7200)
    if pitches is None or pitches is []:
        pitches = aleatoric_freqs(40, 3600, 7200)
        amps = random.sample(range(10, 200), 40)
        amps = [x * -1 for x in amps]
    if len(pitches) != len(amps):
        return None
    index = random.randint(1, 7)
    iterations = 0
    while True:
        iterations += 1
        if iterations > 25:
            pitch_8th = mc2f(4500)
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
            midicent = 4500
            break
        if midicent > 7200:
            midicent = midicent - 1200
        elif midicent < 3600:
            midicent = midicent + 1200
        else:
            break
    pitch, midi_alterations, cents = get_midi_class_of_midicent(midicent)
    alterations = CELLO_8thTones(midi_alterations)
    octave = get_octave(midicent)
    pitch_info = [(pitch, alterations, octave)]
    POSITION = (Mm(0), Mm(0))
    staff = Staff(POSITION, None, Mm(80))
    if midicent > 6200:
        celloClef = 'treble'
    else:
        celloClef = 'bass'

    Clef(ZERO, staff, celloClef)
    # Articulações
    font = Font("Arial", Unit(9), italic=True)
    # TODO: colocar s.p. na Bula
    Text((Unit(20), staff.unit(-6)), staff, "diminuir a cada repetição", font)


    # Chave de repetição
    Barline(Mm(80), staff.group, barline_style.END)
    noteheads = NoteheadTable(
        "repeatDot",
        "repeatDot",
        "repeatDot",
        "repeatDot")

    if celloClef == 'treble':
        note = [('a', '', 4)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('c', '', 5)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
    else:
        note = [('c', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)
        note = [('e', '', 3)]
        Chordrest(Mm(76.5), staff, note, (int(1), int(1)), table=noteheads)

    Chordrest(Mm(5), staff, pitch_info, (int(1), int(1)))
    neoscore.render_image(
        rect=None,
        dest=f'{home}/cello/gesto12.png',
        wait=True,
        dpi=600)
    UpdateRate(
        7000,
        12,
        f'{home}/cello/cello.json',
        frequencyTarget=pitchHz,
        tupletDuration=1167)  # NOTE: 21:17
    pd_print('CELLO_gesto12: Rendered!')
    return "Gesto 12 Rendered!"
