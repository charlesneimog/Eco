from public.functions.utilities.utilities import *
try:
    import pd
    pd_print = pd.print
except:
   pd_print = print 


def CONDUCTOR_GetGestDuration(gestNumber):
    # NOTE: First number is the fluteDur, SaxDur, GuitarDur, CelloDur
    jsonData = {
                "0": [0, 0, 0, 0],
                "1": [6000, 6000, 6000, 6000],
                "2": [3000, 3000, 3000, 3000],
                "3": [15000, 15000, 15000, 15000],
                "4": [17000, 17000, 17000, 17000],
                "5": [22000, 22000, 22000, 22000],
            }
    try:
        durations = jsonData[str(gestNumber)]
    except:
        durations = [0, 0, 0, 0]
    return durations

# ========================================

def CONDUCTOR_UpdateRate(msFlute, msSax, msGuitar, msCello, gesture, file_pathname):
    json_data = {"msFlute": msFlute, "msSax": msSax, "msGuitar": msGuitar, "msCello": msCello, "name": gesture}
    with open(file_pathname, 'w') as out_file:
        json.dump(json_data, out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    return "Conductor Updated!"

# ========================================

def CONDUCTOR_gest(gestNumber):
    home = getHOME_PATH()
    durations = CONDUCTOR_GetGestDuration(gestNumber)
    CONDUCTOR_UpdateRate(durations[0], durations[1], durations[2], durations[3], f"gesto{gestNumber}", f'{home}/conductor/conductor.json')
    return f"Gesto {gestNumber} Rendered!" 



