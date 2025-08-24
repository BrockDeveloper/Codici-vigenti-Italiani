
from .utils import Utils
from ..common import StrCollection
from ..articleParser import Article
from .documentType import DocumentType
from striprtf.striprtf import rtf_to_text
from ..headerParser import HeaderBuilder as Header



class Document:

    '''
    Represents a document, that is a collection of articles. The raw text is
    parsed from a RTF file, and the articles are extracted from it.
    '''

    def __init__(self, document_type: DocumentType):

        '''
        Represents a document, that is a collection of articles. The raw text is
        parsed from a RTF file, and the articles are extracted from it.

        :param documentType: The type of the document to be parsed
        '''

        self.document_type = document_type
        self._plain_text_lines: StrCollection = None
        self._hierarchy: list[dict] = []
        self._articles: list[Article] = []

        self.__load__()


    @property
    def name(self) -> str:

        '''
        :return: The name of the document, formatted as a string
        '''
        
        return self.documentType.name
    

    @property
    def articles(self) -> list[Article]:

        '''
        :return: The list of articles in the document
        '''

        return self._articles
    

    @property
    def hierarchy(self) -> list[dict]:

        '''
        :return: The hierarchy of headers in the document
        '''

        return self._hierarchy
    

    def __load__(self):

        '''
        Load the document from the file path specified in the document type.
        The content is parsed from RTF to plain text, and the plain text is
        split into lines.
        '''

        with open(self.document_type.path, "r", encoding="utf-8") as rtf_file:
            rtf_content = rtf_file.read()

        self._plain_text_lines = StrCollection(rtf_to_text(rtf_content).splitlines())
        self._plain_text_lines.remove_parentheses()
        self._plain_text_lines.remove_empty()

    
    def __parse_header__(self, line_index: int, current_headers: Header):

        '''
        Parse a header from the plain text lines, starting from the given line
        
        :param line_index: The index of the line to start parsing from
        :param current_headers: The current headers state to be updated
        '''

        self._hierarchy.append(
                    current_headers.snapshot_update(
                        Utils.build_header(self._plain_text_lines[line_index],
                                           self._plain_text_lines[line_index+1])))
    

    def __parse_article__(self, line_index: int, current_headers: Header):
        
        '''
        Parse an article from the plain text lines, starting from the given line
        
        :param line_index: The index of the line to start parsing from
        '''

        self._articles.append(
            Article(id = Utils.clean_article_id(self._plain_text_lines[line_index]),
                    content = [],
                    headers = current_headers.progressive_index(),
                    book = self.document_type))


    def parse(self):

        '''
        Parse the document, extracting the articles and the hierarchy of headers.
        '''

        current_headers = Header()
        self._hierarchy = []
        self._articles = []

        i = 0
        while i < len(self._plain_text_lines):

            if Utils.search_header(self._plain_text_lines[i]):
                self.__parse_header__(i, current_headers)
                i += 2 
                continue

            if Utils.search_article(self._plain_text_lines[i]):
                self.__parse_article__(i, current_headers)
                    
            else:
                self._articles[-1].add_content(self._plain_text_lines[i].strip())

            i = i + 1