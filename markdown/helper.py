from enum import Enum

class Syntax(Enum):
    """Supported syntax for adding emphesis to a markdown element"""
    
    b = "**" # Bold
    i = "*"  # Italics

    @classmethod
    def contains(cls, code: str):
        return code in cls._member_names_

class Emphasis:

    @staticmethod
    def withEnphesis(text: str, codes: str = ""):
        """Decorates text with emphesis elements. Any unsupported code will be ignored."""

        values = "".join([Syntax[c].value for c in set(codes.lower()) if Syntax.contains(c)])
        return f"{values}{text}{values}"
    