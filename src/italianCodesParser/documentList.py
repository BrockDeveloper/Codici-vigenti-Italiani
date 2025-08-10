from enum import Enum

class DocumentList(Enum):

    CODICE_PENALE = "././assets/documents/cp.rtf"
    CODICE_CIVILE = "././assets/documents/cp.rtf"

    @property
    def file_path(self):
        return self.value
    
    @property
    def doc_name(self):
        return self.name.replace("_", " ").title()
