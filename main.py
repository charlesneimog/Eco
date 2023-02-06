from python.utilities import *
from python.flute import *
from python.guitar import *
from python.cello import *
from neoscore.common import *

def gesto_functions():
    return [0, 1, 2]

def notesmain():
    global GLOBALPITCHES
    return GLOBALPITCHES

def FLUTE_gesto_generation(gest_number):
    global GLOBALPITCHES
    gest_number = int(gest_number)
    string_of_function = f"FLUTE_gesto{gest_number}()"
    if gest_number in gesto_functions():
        neoscore.setup()
        eval(string_of_function)
        neoscore.shutdown()
    else:
        return "Function not found!"
    return f'Gesto {gest_number} Generated!'
 
 
def SAX_gesto_generation(gest_number):
    return f'Gesto {gest_number} Generated!'


def GUITAR_gesto_generation(gest_number):
    global GLOBALPITCHES
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
    