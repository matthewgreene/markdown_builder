from elements import Header
from lists import CheckboxList, Marker, OrderedList, UnorderedList
from typing import List, Union

class MarkdownBuilder:
    def __init__(self, title: str="") -> None:
        self.title = title
        self.elements = []

    def addHeader(self, level: int, text: str):
        self.elements.append(Header(level=level, text=text))

    def addUnorderedList(self, uol: UnorderedList):
        self.elements.append(uol)

    def addOrderedList(self, ol: OrderedList):
        self.elements.append(ol)

    def addCheckboxList(self, cl: CheckboxList):
        self.elements.append(cl)

    def toStr(self):
        elemStrs = [elem.md_str() for elem in self.elements]
        return "\n".join(elemStrs)