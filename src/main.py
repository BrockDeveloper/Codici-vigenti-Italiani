
import json
from italianCodesParser import Document, DocumentType


doc = Document(DocumentType.CODICE_DI_PROCEDURA_PENALE)
doc.parse()

for article in doc.articles:
    if article.id == "15":
        article.parse()
        print(json.dumps(article.to_dict(), indent=4, ensure_ascii=False))