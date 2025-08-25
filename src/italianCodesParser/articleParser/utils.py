
import re


class Utils:

    '''
    Utility functions for article parsing.
    '''
   
    
    @staticmethod
    def search_update(candidate: str) -> bool:

        '''
        Check if the given string is an update.

        :param candidate: The string to be checked
        :return: True if the string is an update, False otherwise
        '''

        return re.match(r"AGGIORNAMENTO\s*\(\d+[A-Za-z]*\)", candidate)
    

    @staticmethod
    def search_update_id(candidate: str) -> str:

        '''
        Extract the update id from the given string.

        :param candidate: The string to be checked
        :return: The update id if the string is an update, None otherwise
        '''

        return re.search(r'\d+', candidate).group(0)
    

    @staticmethod
    def clean_title(candidate: str) -> str:

        '''
        Clean the title by removing parenteses and stripping whitespace.

        :param candidate: The title to be cleaned
        :return: The cleaned title
        '''

        return re.sub(r"[().]", "", candidate).strip()