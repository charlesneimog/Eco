from public.functions.flute.flute import *
from public.functions.cello.cello import *
from public.functions.guitar.guitar import *
from public.functions.sax.sax import *
from public.functions.conductor.conductor import *
from public.functions.utilities.utilities import *
from neoscore.common import *
from om_py import *
import time
try:
    import pd
    pd_print =  pd.print
except:
    pd_print = print


def set_global_notes(nota):
    set_FLUTE_global_notes(nota)
    set_SAX_global_notes(nota)
    set_GUITAR_global_notes(nota)
    set_CELLO_global_notes(nota)
    return "Global notes updated!"

def set_global_amps(amps):
    set_FLUTE_global_amps(amps)
    set_SAX_global_amps(amps)
    set_GUITAR_global_amps(amps)
    set_CELLO_global_amps(amps)
    return "Global amps updated!"


def clear_global_notes():
    clear_FLUTE_global_notes()
    clear_SAX_global_notes()
    clear_GUITAR_global_notes()
    clear_CELLO_global_notes()
    return "Global notes cleared!"

def clear_global_amps():
    clear_FLUTE_global_amps()
    clear_SAX_global_amps()
    clear_GUITAR_global_amps()
    clear_CELLO_global_amps()
    return "Global amps cleared!"


def set_notesAndAmps(nota, amps):
    set_global_notes(nota)
    set_global_amps(amps)
    return "Notes and amps updated!"

def clear_notesAndAmps():
    clear_global_notes()
    clear_global_amps()
    return "Notes and amps cleared!"


def gesto_functions():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

 
def FLUTE_gesto_generation(gest_number):
    if gest_number == 0:
        pass
    else:
        gest_number = gest_number + 2

    gest_number = int(gest_number)
    string_of_function = f"FLUTE_gesto{gest_number}()"
    if gest_number in gesto_functions():
        neoscore.setup()
        eval(string_of_function)
        neoscore.shutdown()
        CONDUCTOR_gest(gest_number)
    else:
        return "Function not found!"
    return f'Gesto {gest_number} Generated!'
 
 
def SAX_gesto_generation(gest_number):
    if gest_number == 0:
        pass
    else:
        gest_number = gest_number + 2
    gest_number = int(gest_number)
    string_of_function = f"SAX_gesto{gest_number}()"
    if gest_number in gesto_functions():
        neoscore.setup()
        eval(string_of_function)
        neoscore.shutdown()
    else:
        return "Function not found!"
    return f'Gesto {gest_number} Generated!'


def GUITAR_gesto_generation(gest_number):
    if gest_number == 0:
        pass
    else:
        gest_number = gest_number + 2
    gest_number = int(gest_number)
    string_of_function = f"GUITAR_gesto{gest_number}()"
    # check if the function exists
    if gest_number in gesto_functions():
        neoscore.setup()
        eval(string_of_function)
        neoscore.shutdown()
    else:
        return "Function not found!"
    return f'Gesto {gest_number} Generated!'


def CELLO_gesto_generation(gest_number):
    if gest_number == 0:
        pass
    else:
        gest_number = gest_number + 2
    gest_number = int(gest_number)
    string_of_function = f"CELLO_gesto{gest_number}()"
    if gest_number in gesto_functions():
        neoscore.setup()
        eval(string_of_function)
        neoscore.shutdown()
    else:
        return "Function not found!"
    return f'Gesto {gest_number} Generated!'


def ALL_gesto_geration(gest_number):
    start_time = time.time()
    FLUTE_gesto_generation(gest_number)
    SAX_gesto_generation(gest_number)
    GUITAR_gesto_generation(gest_number)
    CELLO_gesto_generation(gest_number)
    CONDUCTOR_gest(gest_number)
    end_time = time.time()
    time_difference = end_time - start_time
    time_difference = round(time_difference * 1000)
    pd_print(f"Time taken to generate gesto {gest_number}: {time_difference} miliseconds")
    return "All gestos number " + str(gest_number) + " generated!"
