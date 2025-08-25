
from .utils import Utils
from .update import Update
from ..common import StrCollection


class Article:

    '''
    Represents an article in the document, with its id, book, title, content,
    updates, and headers.
    '''

    def __init__(self, id: str = None, book: str = None, title: str = None, 
                 content: list[str] = [], updates: list[Update ] = [], headers:str = None):
        
        '''
        Represents an article in the document, with its id, book, title, content,
        updates, and headers.
        
        :param id: The id of the article
        :param book: The book of the article
        :param title: The title of the article
        :param content: The raw content of the article, not parsed
        :param updates: The list of updates of the article
        :param headers: The headers of the article
        '''

        self.id = id
        self.book = book
        self.title = title
        self.content = StrCollection(content)
        self.headers = headers
        self.updates = updates


    def add_content(self, new_content: str):

        '''
        Add new content to the article.
        
        :param new_content: The new content to be added
        '''

        self.content.append(new_content)

    
    def __updates_list__(self):

        '''
        :return: The content of the updates as a list of strings
        '''

        updates = []
        for update in self.updates:
            updates.append(update.to_str())

        return updates

   
    def __parse_title__(self):

        '''
        Parse the title of the article from its content, if the book has titles.
        '''

        if self.content and self.book.has_titles():
            self.title = Utils.clean_title(self.content[0])
            self.content.pop()
    

    def __parse_updates__(self):

        '''
        Parse the updates from the raw content of the article. Only when the
        first update is found, the following lines are considered part of the
        update, until another update is found or the end of the content is reached.
        '''

        i = 0
        while i < len(self.content):

            if Utils.search_update(self.content[i]):
                self.updates.append(
                    Update(id=Utils.search_update_id(self.content[i]),
                           content=[]))
                self.content[i] = None

            else:
                if self.updates:
                    self.updates[-1].content.append(self.content[i])
                    self.content[i] = None

            i = i + 1
    

    def __parse_content__(self):

        '''
        Clean the content of the article, removing links to updates, parentheses,
        and trimming spaces. Transform the raw content into a list of strings
        that represent the paragraphs of the article.
        '''
        
        self.content.clean_cite_links([update.id for update in self.updates])
        self.content.remove_parentheses()
        self.content.remove_residual_parentheses()
        self.content.strip()
    

    def parse(self):

        '''
        Preprocess the text of the article, parsing the title and the updates.
        '''
        
        self.content.clean_content()
        self.__parse_title__()
        self.__parse_updates__()
        self.content.clean_content()
        self.__parse_content__()
        

    def to_dict(self):

        '''
        :return: The article as a dictionary
        '''
        
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content.to_list(),
            "updates": self.__updates_list__(),
            "headers": self.headers
        }