

class Update:

    '''
    Represents an update in the article.
    '''

    def __init__(self, id: str, content: list[str]):

        self.id = id
        self._content = content


    def to_list(self) -> list[str]:

        '''
        :return: The content of the update as a list of strings
        '''
        
        return self._content