from __future__ import annotations

from enum import Enum
from typing import List, Union

class Marker(Enum):
        ASTERISK    = "*"
        CHECKBOX    = "- [ ]"   
        DASH        = "-"
        NUMBER      = "1."
        PLUS        = "+"


class BaseList():
    """
    Base class for creating lists in Markdown. Lists can be nested by including 
    a new `BaseList` object in the item list.
    """

    def __init__(self, items: List[Union[str, BaseList]], marker: Marker) -> None:
        """
        Initialize a new list.

        :param items:  Elements which the list is created from. Allowed item types are `str` and `BaseList`.
        :param marker: Character for specifying the items of the list. Default is `Marker.DASH`
        """

        for item in items:
            self.__validateItem(item=item)
        self.items = items
        self.marker = marker
            
    def __validateItem(self, item: Union[str, BaseList]) -> None:
        """
        Validation to ensure only a list item is of type `str` and `BaseList` only.
        :param item: Item to be validated against.
        """

        if not (isinstance(item, str) or isinstance(item, BaseList)):
            raise ValueError(f"Invalid item type. Expected ['str', 'BaseList']. Received {type(item)}")
            
    def add(self, item: Union[str, BaseList]) -> None:
        """
        Add new item to list
        """

        self.__validateItem(item=item)
        self.items.append(item)
        
    def md_str(self, padding: str = ""):
        """
        Concrete implementation of abstract method. Loops through each item and creates Markdown strings.
        Nested lists are padded with four spaces.
        """
        
        out = []
        for item in self.items:
            if isinstance(item, str):
                out.append(f"{padding}{self.marker.value} {item}")
            else:
                out.append("".join(item.md_str(padding=padding+"    ")))

        return "\n".join(out)
    


class UnorderedList(BaseList):
    "Implementation for creating unordered lists."
    
    def __init__(self, items: List[Union[str, UnorderedList]] = [], marker: Marker = Marker.DASH) -> None:
        allowed_markers = [Marker.ASTERISK, Marker.DASH, Marker.PLUS]
        if marker not in allowed_markers:
            raise ValueError(f"Invalid marker: Allowed {[m.value for m in allowed_markers]}, recieved [{marker.value}]")
        super().__init__(items=items, marker=marker)


class OrderedList(BaseList):
    "Implementation for creating ordered lists."

    def __init__(self, items: List[str | List]) -> None:
        super().__init__(items, Marker.NUMBER)


class CheckboxList(BaseList):
    "Implementation for creating checkbox lists."

    def __init__(self, items: List[str | List]) -> None:
        super().__init__(items, Marker.CHECKBOX)
    