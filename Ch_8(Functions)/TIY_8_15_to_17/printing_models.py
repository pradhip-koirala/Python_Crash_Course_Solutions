# import printing_functions as pf

# 8.16 imports
import printing_functions

from printing_functions import print_models,show_completed_models

from printing_functions import print_models as pm,show_completed_models as scm

import printing_functions as pf

from printing_functions import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs,completed_models)
scm(completed_models)