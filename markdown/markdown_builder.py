from elements import Header
from lists import CheckboxList, Marker, OrderedList, UnorderedList
from typing import List, Union

class MarkdownBuilder:
    """
    This class contains methods for constructing Markdown files.
    """

    def __init__(self, title: str="") -> None:
        self.title = title
        self.elements = []

    def addHeader(self, level: int, text: str):
        """Adds new header elements to the Markdown file."""
        
        self.elements.append(Header(level=level, text=text))

    def addUnorderedList(self, uol: UnorderedList):
        """Adds new unordered lists to the Markdown file"""

        self.elements.append(uol)

    def addOrderedList(self, ol: OrderedList):
        """Adds new ordered lists to the Markdown file"""

        self.elements.append(ol)

    def addCheckboxList(self, cl: CheckboxList):
        """Adds new checkbox lists to the Markdown file"""

        self.elements.append(cl)

    def toStr(self):
        """Returns the Markdown elements as strings to be writing to file."""

        elemStrs = [elem.md_str() for elem in self.elements]
        return "\n".join(elemStrs)
    
    # TODO: Implements file writing functionality