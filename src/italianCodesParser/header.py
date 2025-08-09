from dataclasses import dataclass

@dataclass
class Header:

    LIBRO: str = None
    TITOLO: str = None
    CAPO: str = None
    Sezione: str = None

    def to_dict(self):
        return {
            "LIBRO": self.LIBRO,
            "TITOLO": self.TITOLO,
            "CAPO": self.CAPO,
            "Sezione": self.Sezione
        }