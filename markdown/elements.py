import abc
from typing import List, Union
from enum import Enum

class BaseElement(abc.ABC):
    @abc.abstractmethod
    def md_str(self) -> str:
        pass


class Header(BaseElement):
    def __init__(self, level: int, text: str) -> None:
        super().__init__()
        if not (1 <= level <= 6):
            raise ValueError("Header level should be between 1 and 6")
        self.level = level
        self.text = text
    
    def md_str(self) -> str:
        return f"{'#'*self.level} {self.text}"

