
import re
from ..headerParser import Header
from ..common import StrCollection


class Utils:

    '''
    Utility functions for document parsing.
    '''

    @staticmethod
    def search_article(candidate: str) -> bool:

        '''
        Check if the given string is an article identifier.

        :param candidate: The string to be checked
        :return: True if the string is an article identifier, False otherwise
        '''

        return re.search(r'Art\. \d+(-[a-z]+)?\.?$', candidate.strip())
   
    
    @staticmethod
    def search_header(candidate: str) -> bool:

        '''
        Check if the given string is an header.

        :param candidate: The string to be checked
        :return: True if the string is an header, False otherwise
        '''

        return re.search(r'^(LIBRO|TITOLO|CAPO|Sezione|Libro|Titolo|Capo) \w+\.?$', 
                         candidate.strip())
    

    @staticmethod
    def clean_article_id(candidate: str) -> str:

        '''
        Clean the article identifier by removing the "Art. " prefix and the
        trailing dot.

        :param candidate: The article identifier to be cleaned
        :return: The cleaned article identifier
        '''

        return candidate.replace("Art. ", "").replace(".", "").strip()
    

    @staticmethod
    def build_header(candidate: str, name_candidate: str) -> Header:

        '''
        Build a Header object from the given string.

        :param candidate: The string containing the header type and id
        :param name_candidate: The string containing the header name
        :return: The Header object
        '''

        parsed = StrCollection(candidate.split(" "))
        parsed.remove_empty()
        parsed.strip()

        header_type = parsed[0]
        header_id = parsed[1]

        header_name = name_candidate.split("<br/>")[0].strip()

        return Header(
            id=header_id,
            name=header_name,
            type=header_type.upper(),
            progressive=None)