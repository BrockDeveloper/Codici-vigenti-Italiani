
import re


class StrCollection:

    '''
    A collection of strings with some utility methods.
    '''

    def __init__(self, strings: list[str]):

        '''
        A collection of strings with some utility methods.

        :param strings: A list of strings to be stored in the collection
        '''

        self._strings = strings

    
    def append(self, string: str):

        '''
        Append a string to the collection.

        :param string: The string to be appended
        '''

        self._strings.append(string)
    

    def pop(self):
        
        '''
        Pop the first string from the collection.
        '''

        self._strings = self._strings[1:]


    
    def remove_parentheses(self):

        '''
        Remove all parentheses from the strings in the collection.
        '''

        pattern = r'\(\(|\)\)'
        self._strings = [re.sub(pattern, '', s) for s in self._strings]


    def strip(self):

        '''
        Strip all strings in the collection.
        '''

        self._strings = [s.strip() for s in self._strings]

    
    def remove_empty(self):

        '''
        Remove all empty strings from the collection.
        '''

        self._strings = [s for s in self._strings if s.strip()]

    
    def clean_content(self):

        '''
        Remove all empty lines and lines that are just text separators.
        '''

        self._strings = [s for s in self._strings if s is not None
                         and not re.match(r"^-+$", s)]
    

    def clean_cite_links(self, numeric_references: list[str]):

        '''
        Remove all citations to updates from the strings in the collection.

        :param numeric_references: A list of numeric references to be removed
        '''

        pattern = r"|".join(map(re.escape, numeric_references))
        self._strings = [re.sub(pattern, "", s) for s in self._strings]
    

    def __len__(self) -> int:

        '''
        :return: The number of strings in the collection
        '''

        return len(self._strings)
    

    def __getitem__(self, index: int) -> str:

        '''
        Get the string at the specified index.

        :param index: The index of the string to be retrieved
        :return: The string at the specified index
        '''

        return self._strings[index]
    

    def __setitem__(self, index: int, value: str):

        '''
        Set the string at the specified index.

        :param index: The index of the string to be set
        :param value: The string to be set at the specified index
        '''

        self._strings[index] = value
    

    def __iter__(self) -> iter:

        '''
        :return: An iterator over the strings in the collection
        '''

        return iter(self._strings)
    

    def to_list(self) -> list[str]:

        '''
        :return: The strings in the collection as a list
        '''

        return self._strings