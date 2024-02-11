from .header import Header
from .helper import Syntax, Emphasis
from .list import BaseList, CheckboxList, Marker, OrderedList, UnorderedList
from .paragraph import Paragraph
from .table import Table
from typing import List, Union

class MarkdownBuilder:
    """
    This class contains methods for constructing Markdown files.
    """

    def __init__(self) -> None:
        self.elements = []

    def addHeader(self, level: int, text: str):
        """Adds new header elements to the Markdown file."""
        
        self.elements.append(Header(level=level, text=text))

    def addList(self, mdList: BaseList):
        """Adds a new list to the Markdown file"""
        self.elements.append(mdList)

    def addTable(self, table: Table):
        """Adds new table elements to the Markdown file"""

        self.elements.append(table)

    def addParagraph(self, text: str):
        """Adds new paragraph elements to the Markdown file"""

        self.elements.append(Paragraph(text))

    def createLink(self, url: str, text: str, alt: str = "", emphesis: str = "") -> str:
        """Creates new link elements"""
        
        if emphesis:
            text = Emphasis.withEnphesis(text=text, codes=emphesis)

        return f"[{text}]({url} \"{alt}\")"

        

    def toStr(self):
        """Returns the Markdown elements as strings to be writing to file."""

        elemStrs = [elem.md_str() for elem in self.elements]
        return "\n".join(elemStrs)
    
    def write(self, path: str):
        """Writes Markdown elements to specified file path"""

        with open(path, "w+") as file:
            markdown = self.toStr()
            file.write(markdown)