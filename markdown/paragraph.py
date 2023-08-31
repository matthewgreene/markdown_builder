from .elements import BaseElement

class Paragraph(BaseElement):
    """Class for creating paragraph elements"""

    def __init__(self, text: str) -> None:
        super().__init__()
        self.text = text

    def md_str(self) -> str:
        """Paragraphs are simply blocks of text separated by a new line."""
        return self.text + "\n"
