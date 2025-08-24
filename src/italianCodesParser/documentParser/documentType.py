
from enum import Enum


class DocumentType(Enum):

    '''
    List of documents types, i.e. the list of documents that can be parsed.
    Each document type has a name and a file path.
    '''

    CODICE_PENALE = "././assets/documents/cp.rtf"
    CODICE_CIVILE = "././assets/documents/cc.rtf"
    CODICE_DI_PROCEDURA_PENALE = "././assets/documents/cpp.rtf"
    CODICE_DI_PROCEDURA_CIVILE = "././assets/documents/cpc.rtf"
    ATTUAZIONE_CODICE_CIVILE = "././assets/documents/attcc.rtf"
    ATTUAZIONE_CODICE_DI_PROCEDURA_CIVILE = "././assets/documents/attcpc.rtf"
    ATTUAZIONE_CODICE_DI_PROCEDURA_PENALE = "././assets/documents/attcpp.rtf"


    @property
    def path(self) -> str:

        '''
        :return: The file path of the document type
        '''
        
        return self.value
    

    @property
    def name(self) -> str:

        '''
        :return: The name of the document type, formatted as a string
        '''
        
        return self.name.replace("_", " ").title()
    

    def has_titles(self) -> bool:

        '''
        :return: True if the document type has titles, False otherwise
        '''

        return self in {DocumentType.CODICE_PENALE, 
                        DocumentType.CODICE_CIVILE,
                        DocumentType.CODICE_DI_PROCEDURA_PENALE,
                        DocumentType.CODICE_DI_PROCEDURA_CIVILE,
                        DocumentType.ATTUAZIONE_CODICE_DI_PROCEDURA_PENALE,
                        DocumentType.ATTUAZIONE_CODICE_DI_PROCEDURA_CIVILE}