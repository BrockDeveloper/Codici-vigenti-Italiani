
from .headerType import HeaderType


class Header:

    '''
    Represents a header in the Italian legal codes.
    '''

    def __init__(self, id: str, name: str, type: HeaderType, progressive: str):

        '''
        Represents a header in the Italian legal codes.
        
        :param id: The id of the header
        :param name: The name of the header
        :param type: The type of the header
        :param progressive: The progressive index of the header
        '''

        self.id = id
        self.name = name
        self.type = type
        self.progressive = progressive