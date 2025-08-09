from dataclasses import dataclass

@dataclass
class Update:

    id: str
    content: list[str]


    def to_dict(self):
        return self.content