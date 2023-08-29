from __future__ import annotations

import abc
from typing import List, Union
from enum import Enum

class BaseElement(abc.ABC):
    """
    Base class for creating elements in Markdown.
    Class which extend the `BaseElement` must implement the `md_str` method
    """

    @abc.abstractmethod
    def md_str(self) -> str:
        """Abstract method for converting elements to Markdown strings"""


class Header(BaseElement):
    """Class for creating header elements.
    """
    def __init__(self, level: int, text: str) -> None:
        """
        Initialize new header
        
        :param level: The number of hashes (#) to be used when creating the header. Valid headers are 1-6.
        :param text: The text to be displayed in the header.
        """

        super().__init__()
        if not (1 <= level <= 6):
            raise ValueError("Header level should be between 1 and 6")
        self.level = level
        self.text = text
    
    def md_str(self) -> str:
        return f"{'#'*self.level} {self.text}"

class Row(BaseElement):
    def __init__(self, cells: List[str]) -> None:
        self.cells = cells

    def md_str(self) -> str:
        return f"|{'|'.join(self.cells)}|"

class TableAlign(Enum):
    CENTER = ":---:"
    LEFT   = ":---"
    RIGHT  = "---:"
    

class Table(BaseElement):
    """Class for creating table elements"""

    def __init__(
            self, 
            rows: List[Row] = [], 
            align: TableAlign = TableAlign.LEFT
        ) -> None:
        """We can assume the first row is the header row."""
        super().__init__()
        self.rows = rows
        self.align = align

    def addRow(self, row: Row) -> None:
        self.rows.append(row)
    
    def _header_alignment(self) -> str:
        alignment = [self.align.value for _ in self.rows[0].cells]
        return f"|{'|'.join(alignment)}|"

    def md_str(self) -> str:
        row_strs = [row.md_str() for row in self.rows]
        row_strs.insert(1, self._header_alignment())
        return "\n".join(row_strs)
        
        
