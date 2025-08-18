from .headerParser.headerBuilder import Header
from .update import Update
import re

class Article:

    def __init__(self, id=None, book=None, title=None, content=[], updates=[],headers=Header()):

        self.id = id
        self.book = book
        self.title = title
        self.content = content
        self.headers = headers
        self.updates = updates

    def add_content(self, new_content):
        self.content.append(new_content)
    

    def parse_content(self):

        # Remove all empty lines and lines that are just text separators
        self.content = [line_content for line_content in self.content 
                        if line_content is not None
                        and not re.match(r"^-+$", line_content)]
        
        # Remove links to the updates
        update_ids = [update.id for update in self.updates]
        pattern_update_ids = r"|".join(map(re.escape, update_ids))

        self.content = [re.sub(pattern_update_ids, "", line_content) for line_content in self.content]




    def parse_title(self):
        if self.content:
            self.title = self.content[0]
            self.content = self.content[1:]

            self.title = re.sub(r"[().]", "", self.title)

    def parse_updates(self):

        i = 0
        while i < len(self.content):

            if re.match(r"AGGIORNAMENTO\s*\(\d+\)", self.content[i]):

                self.updates.append(
                    Update(
                        id=re.search(r'\d+', self.content[i]).group(0),
                        content=[]
                    )
                )
                # Sign to remove
                self.content[i] = None
            else:
                if self.updates:
                    self.updates[-1].content.append(self.content[i])
                    # Sign to remove
                    self.content[i] = None

            i = i + 1

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "updates": [update.to_dict() for update in self.updates],
            "headers": self.headers.to_dict()
        }