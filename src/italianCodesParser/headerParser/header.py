
from dataclasses import dataclass
from .headerType import HeaderType

@dataclass
class Header:

    id: str = None
    name: str = None
    type: HeaderType = None
    progressive: str = None