from enum import Enum

class Syntax(Enum):
    """Supported syntax for adding emphesis to a markdown element"""

    b = "**" # Bold
    i = "*"  # Italics
    c = "`"  # Code

    @classmethod
    def contains(cls, code: str):
        return code in cls._member_names_

class Emphasis:

    @staticmethod
    def withEnphesis(text: str, codes: str = ""):
        """Decorates text with emphesis elements. Any unsupported code will be ignored."""
        
        values = [Syntax[c].value for c in codes.lower() if Syntax.contains(c)]
        begin = "".join(values)
        end = "".join(values[::-1])

        return f"{begin}{text}{end}"
    