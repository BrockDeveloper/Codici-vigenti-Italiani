
from enum import Enum


class HeaderType(Enum):

    '''
    List of header types, i.e. the list of headers that can be parsed.
    The hierarchy is as follows: Libro, Titolo, Capo, Sezione.
    '''

    LIBRO = "LIBRO"
    TITOLO = "TITOLO"
    CAPO = "CAPO"
    SEZIONE = "Sezione"