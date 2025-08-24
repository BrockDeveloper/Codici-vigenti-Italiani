

from italianCodesParser.documentParser.document import Document
from italianCodesParser.documentParser.documentType import DocumentType

doc = Document(DocumentType.ATTUAZIONE_CODICE_DI_PROCEDURA_PENALE)
doc.build()



for article in doc.articles:



    if article.id == "25":

        article.text_preprocess()
        article.parse_title()
        article.parse_updates()
        article.parse_content()
        import json
        print(json.dumps(article.to_dict(), indent=4, ensure_ascii=False))