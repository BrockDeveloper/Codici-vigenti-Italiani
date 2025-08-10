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
    
    def get_hierarchy(self, header_type: str, header_id: str, header_name: str):

        # Give every header a successive number, starting from 0, so it can get
        # the parent header by substrating one from the current header
        hierarchy = {
            "LIBRO": 1,
            "TITOLO": 2,
            "CAPO": 3,
            "Sezione": 4
        }

        parent_type = None
        parent_id = None
        parent_name = None #!TODO deve fornire anche il nome
        if hierarchy[header_type] - 1 > 0:
            parent_type = list(hierarchy.keys())[hierarchy[header_type] - 2]
            parent_id = getattr(self, parent_type, None)
        

        return {
            "type": header_type,
            "id": header_id,
            "name": header_name,
            "parent_type": parent_type,
            "parent_id": parent_id
        }