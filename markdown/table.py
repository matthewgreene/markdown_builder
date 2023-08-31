from .elements import BaseElement
from typing import List
from enum import Enum

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