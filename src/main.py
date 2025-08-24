
import json
from italianCodesParser import Document, DocumentType


doc = Document(DocumentType.CODICE_CIVILE)
doc.parse()

for article in doc.articles:
    if article.id == "25":
        article.parse()
        print(json.dumps(article.to_dict(), indent=4, ensure_ascii=False))