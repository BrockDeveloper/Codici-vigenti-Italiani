from dataclasses import dataclass

@dataclass
class Update:

    id: str
    content: list[str]


    def to_list(self):
        return self.content