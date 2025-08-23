
import re
from .documentType import DocumentType
from ..headerParser.headerBuilder import HeaderBuilder as Header
from striprtf.striprtf import rtf_to_text
from ..articleParser.article import Article


class Document:

    '''
    Represents a document, that is a collection of articles. The raw text is
    parsed from a RTF file, and the articles are extracted from it.
    '''

    def __init__(self, document_type: DocumentType):

        '''
        :param documentType: The type of the document to be parsed
        '''

        self.document_type = document_type
        self._plain_text_lines = None
        self._hierarchy = None
        self._articles = None

        self.__load__()
    

    @property
    def name(self):

        '''
        :return: The name of the document, formatted as a string
        '''
        
        return self.documentType.name
    

    def __load__(self):

        '''
        Load the document from the file path specified in the document type.
        The content is parsed from RTF to plain text, and the plain text is
        split into lines.
        '''

        with open(self.document_type.path, "r", encoding="utf-8") as rtf_file:
            rtf_content = rtf_file.read()

        plain_text = rtf_to_text(rtf_content)
        plain_text = re.sub(r'\(\(|\)\)', '', plain_text)
        plain_text_lines = plain_text.splitlines()

        self._plain_text_lines = [line for line in plain_text_lines if line.strip()]
    

    @property
    def articles(self):
        return self._articles
    

    @property
    def hierarchy(self):
        return self._hierarchy


    def build(self):

        current_headers = Header()
        self._hierarchy = []
        self._articles = []

        i = 0
        while i < len(self._plain_text_lines):

            # Search for headers
            if re.search(r'^(LIBRO|TITOLO|CAPO|Sezione) \w+$', 
                         self._plain_text_lines[i].strip()):
                
                # Parse the header and the next line as the name of the header
                parsed_header = self._plain_text_lines[i].split(" ")
                parsed_header = [split.strip() for split in parsed_header if split.strip()]
                header_type, header_id = parsed_header[0].strip(), parsed_header[1].strip()

                i = i + 1
                header_name = self._plain_text_lines[i].strip()
                header_name = header_name.split("<br/>")[0]

                # Get the hierarchy of the current header
                self._hierarchy.append(
                    current_headers.snapshot_update(header_type, header_id, header_name)
                )

                # Move to the next iteration
                i = i + 1
                continue

            # If the line is not empy, it can be an article. It is recognizable by the 
            # fact that it contains the sentence "Art. " followe by a number and,
            # eventually, a dash with a latin specifier and a dot at the end, no more
            # letters or numbers after the dot
            if re.search(r'Art\. \d+(-[a-z]+)?\.?$', self._plain_text_lines[i].strip()):

                # Surely, the line after the article is the title of the article itself
                self._articles.append(
                    Article(
                        id=self._plain_text_lines[i].replace("Art. ", "").replace(".", "").strip(),
                        content=[],
                        headers=current_headers.progressive_index(),
                    )
                )
                    
            # If there is not a reference to an article, it is the body of the article.
            else:
                self._articles[-1].add_content(self._plain_text_lines[i].strip())


            # Move to the next line
            i = i + 1