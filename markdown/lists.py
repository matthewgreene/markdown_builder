from __future__ import annotations

from enum import Enum
from typing import List, Union

class Marker(Enum):
        DASH = "-"
        ASTERISK = "*"
        PLUS = "+"
        NUMBER = "1."
        CHECKBOX = "- [ ]"   


class BaseList():

    def __init__(self, items: List[Union[str, BaseList]], marker: Marker) -> None:
        for item in items:
            self.__validateItem(item=item)
        self.items = items
        self.marker = marker
            
    def __validateItem(self, item: Union[str, BaseList]) -> None:
        if not (isinstance(item, str) or isinstance(item, BaseList)):
            raise ValueError(f"Invalid item type. Expected ['str', 'BaseList']. Received {type(item)}")
            
    def add(self, item: Union[str, BaseList]) -> None:
        self.__validateItem(item=item)
        self.items.append(item)
        
    def md_str(self, padding: str = ""):
        out = []
        for item in self.items:
            if isinstance(item, str):
                out.append(f"{padding}{self.marker.value} {item}")
            else:
                out.append("".join(item.md_str(padding=padding+"    ")))

        return "\n".join(out)
    


class UnorderedList(BaseList):
    
    def __init__(self, items: List[Union[str, UnorderedList]] = [], marker: Marker = Marker.DASH) -> None:
        allowed_markers = [Marker.ASTERISK, Marker.DASH, Marker.PLUS]
        if marker not in allowed_markers:
            raise ValueError(f"Invalid marker: Allowed {[m.value for m in allowed_markers]}, recieved [{marker.value}]")
        super().__init__(items=items, marker=marker)

    def addItem(self, item: Union[str, UnorderedList]):
        self.items.append(item)


class OrderedList(BaseList):

    def __init__(self, items: List[str | List]) -> None:
        super().__init__(items, Marker.NUMBER)


class CheckboxList(BaseList):

    def __init__(self, items: List[str | List]) -> None:
        super().__init__(items, Marker.CHECKBOX)
    