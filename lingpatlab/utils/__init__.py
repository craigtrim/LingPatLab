from .bp import *
from .svc import *
from .dmo import *
from .dto import *

from .svc.find_wordnet import FindWordnet
from .os import *


def is_wordnet_term(input_text: str) -> bool:
    return FindWordnet().exists(input_text)
