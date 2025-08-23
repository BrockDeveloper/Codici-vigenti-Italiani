
from .header import Header
from .headerType import HeaderType

class HeaderBuilder:

    '''
    Represents a header in the Italian legal codes.
    This class is used to manage the hierarchy of headers such as LIBRO, TITOLO,
    CAPO, and Sezione.
    '''

    def __init__(self):

        self._headers = {
            "LIBRO": Header(None, None, HeaderType.LIBRO, None),
            "TITOLO": Header(None, None, HeaderType.TITOLO, None),
            "CAPO": Header(None, None, HeaderType.CAPO, None),
            "Sezione": Header(None, None, HeaderType.SEZIONE, None)
        }

        self._progressive: dict = {
            "LIBRO": 0,
            "TITOLO": 0,
            "CAPO": 0,
            "Sezione": 0
        }


    def progressive_index(self):

        '''
        Returns the current progressive index as a string in the format:
        "LIBRO.TITOLO.CAPO.Sezione"
        '''

        return ".".join(str(self._progressive[key]) 
                        for key in ["LIBRO", "TITOLO", "CAPO", "Sezione"])
   
   
    def snapshot_update(self, header_type: str, header_id: str, header_name: str):
    
        '''
        Update the header to the current header type.
        
        :param header_type: The type of the header (LIBRO, TITOLO, CAPO, Sezione)
        :param header_id: The ID of the header
        :param header_name: The name of the header
        '''

        updated: bool = False
        for digit in self._progressive:

            if digit == header_type:
                self._progressive[digit] += 1
                updated = True
            else:
                if updated:
                    self._progressive[digit] = 0

        self._headers[header_type].id = header_id
        self._headers[header_type].name = header_name    
        self._headers[header_type].progressive = self.progressive_index()
        
        return {
            "progressive": self.progressive_index(),
            "type": header_type,
            "id": header_id,
            "name": header_name,
        }