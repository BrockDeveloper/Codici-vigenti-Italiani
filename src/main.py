
# import re
# from striprtf.striprtf import rtf_to_text
# from italianCodesParser.header import Header
# from italianCodesParser.article import Article
# from italianCodesParser.documentList import DocumentList

from italianCodesParser.document import Document
from italianCodesParser.documentList import DocumentList

doc = Document(DocumentList.CODICE_PENALE, load=True)

import json
print(json.dumps(doc.build_headers_hierarchy(), indent=4, ensure_ascii=False))


exit(0)

with open("./assets/documents/cp.rtf", "r", encoding="utf-8") as file:
    rtf_content = file.read()

plain_text = rtf_to_text(rtf_content)



# List of articles parsed, and the current headers to be used
articles = []
current_headers = Header()

# Use index access so it can skip some indexes when needed
i = 0
while i < len(plain_text_lines):

    # Ignore everything is related to the headers, 
    # and the next line because it is the name of the header
    if re.search(r'^(LIBRO|TITOLO|CAPO|Sezione) \w+$', plain_text_lines[i].strip()):

        parsed_header = plain_text_lines[i].split(" ", 1)
        setattr(current_headers, parsed_header[0].strip(), parsed_header[1].strip())

        i = i + 2
        continue

    # If te line is not empy, it can be an article. It is recognizable by the 
    # fact that it contains the sentence "Art. " followe by a number and,
    # eventually, a dash with a latin specifier and a dot at the end, no more
    # letters or numbers after the dot
    if re.search(r'Art\. \d+(-[a-z]+)?\.?$', plain_text_lines[i].strip()):

        # Surely, the line after the article is the title of the article itself
        articles.append(
            Article(
                id=plain_text_lines[i].replace("Art. ", "").replace(".", "").strip(),
                content=[],
                headers=current_headers
            )
        )
     
    # If there is not a reference to an article, it is the body of the article.
    else:
        articles[-1].add_content(plain_text_lines[i].strip())

    # Move to the next line
    i = i + 1


for article in articles:

    if article.id == "705":

        article.parse_title()
        article.parse_updates()
        article.parse_content()
        import json
        print(json.dumps(article.to_dict(), indent=4, ensure_ascii=False))