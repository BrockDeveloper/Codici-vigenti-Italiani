
from .header import Header
from .headerType import HeaderType


class HeaderBuilder:

    '''
    Represents a header in the Italian legal codes.
    This class is used to build the hierarchy of headers.
    '''

    def __init__(self):

        '''
        Represents a header in the Italian legal codes.
        This class is used to build the hierarchy of headers.
        '''

        # Actual headers information
        self._headers = {
            "LIBRO": Header(None, None, HeaderType.LIBRO, None),
            "TITOLO": Header(None, None, HeaderType.TITOLO, None),
            "CAPO": Header(None, None, HeaderType.CAPO, None),
            "SEZIONE": Header(None, None, HeaderType.SEZIONE, None)
        }

        # Actual progressive index of the headers
        self._progressive: dict = {
            "LIBRO": 0,
            "TITOLO": 0,
            "CAPO": 0,
            "SEZIONE": 0
        }


    def progressive_index(self) -> str:

        '''
        Returns the current progressive index as a string in the format:
        "LIBRO.TITOLO.CAPO.Sezione"
        '''

        return ".".join(str(self._progressive[key]) 
                        for key in ["LIBRO", "TITOLO", "CAPO", "SEZIONE"])
    

    def __progressive_update__(self, header_type: HeaderType):

        '''
        Update the header to the current header type.
        
        :param header_type: The type of the header to be updated
        '''

        updated: bool = False
        for digit in self._progressive:

            if digit == header_type:
                self._progressive[digit] += 1
                updated = True
            else:
                if updated:
                    self._progressive[digit] = 0
   
   
    def snapshot_update(self, header: Header) -> dict:
    
        '''
        Update the header to the current header type.
        
        :param header: The header to be updated
        :return: A snapshot of the current header state as a dictionary
        '''

        self.__progressive_update__(header.type)
        self._headers[header.type] = header 
        
        return {
            "progressive": self.progressive_index(),
            "type": header.type,
            "id": header.id,
            "name": header.name
        }