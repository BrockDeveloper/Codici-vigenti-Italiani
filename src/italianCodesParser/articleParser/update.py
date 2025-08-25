

class Update:

    '''
    Represents an update in the article.
    '''

    def __init__(self, id: str, content: list[str]):

        self.id = id
        self.content = content


    def to_str(self) -> str:

        '''
        :return: The content of the update as a list of strings
        '''
        
        return " ".join(self.content)