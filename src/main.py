

from italianCodesParser.documentParser.document import Document
from italianCodesParser.documentParser.documentType import DocumentType

doc = Document(DocumentType.CODICE_PENALE)
doc.build()


for article in doc.articles:

    if article.id == "678":

        article.parse_title()
        article.parse_updates()
        article.parse_content()
        import json
        print(json.dumps(article.to_dict(), indent=4, ensure_ascii=False))