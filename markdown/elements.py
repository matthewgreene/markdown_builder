from __future__ import annotations

import abc

class BaseElement(abc.ABC):
    """
    Base class for creating elements in Markdown.
    Class which extend the `BaseElement` must implement the `md_str` method
    """

    @abc.abstractmethod
    def md_str(self) -> str:
        """Abstract method for converting elements to Markdown strings"""
        
