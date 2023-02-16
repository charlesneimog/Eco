from public.functions.flute.flute import *
from public.functions.sax.sax import *
from public.functions.guitar.guitar import *
from public.functions.cello.cello import *
from public.functions.utilities.utilities import *

try:
    import pd
    pd_print = pd.print
except:
    pd_print = print 
  
gestnumber = 12
instrument = 1
instruments = ['FLUTE', 'SAX', 'GUITAR', 'CELLO']
neoscore.setup()
eval(instruments[instrument] + '_gesto' + str(gestnumber) + '()')
neoscore.show(display_page_geometry=False)
neoscore.shutdown()

