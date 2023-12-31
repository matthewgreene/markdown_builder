from .elements import BaseElement

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