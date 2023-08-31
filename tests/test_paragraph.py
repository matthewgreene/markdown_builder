import pytest
from markdown.paragraph import Paragraph

def test_paragraph():
    text = "Test paragraph"
    assert Paragraph(text).md_str() == text + "\n"