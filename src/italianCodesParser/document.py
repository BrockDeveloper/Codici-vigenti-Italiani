
import re
from .documentList import DocumentList
from .header import Header
from striprtf.striprtf import rtf_to_text

class Document:

    def __init__(self, documentType: DocumentList, load: bool = True):

        self.documentType = documentType
        self._plain_text_lines = None

        if load:
            self.load()
    

    @property
    def name(self):
        return self.documentType.name
    

    def load(self):

        with open(self.documentType.file_path, "r", encoding="utf-8") as rtf_file:
            rtf_content = rtf_file.read()

        plain_text = rtf_to_text(rtf_content)
        self.__init_plain_text__(plain_text)
    
 
    def __init_plain_text__(self, plain_text: str):

        # Remove all (( and )) from the text
        plain_text = re.sub(r'\(\(|\)\)', '', plain_text)

        # Split the text into lines
        plain_text_lines = plain_text.splitlines()

        # remove all empty lines
        self._plain_text_lines = [line for line in plain_text_lines if line.strip()]
    

    def build_headers_hierarchy(self):

        current_headers = Header()
        hierarchy = []

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

                # Set as the current header, in his hierarchy type
                setattr(current_headers, header_type, header_id)

                # Get the hierarchy of the current header
                hierarchy.append(
                    current_headers.get_hierarchy(header_type, header_id, header_name)
                )
            
            i = i + 1

        return hierarchy