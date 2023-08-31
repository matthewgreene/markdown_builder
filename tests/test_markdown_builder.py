import os
import pytest
import tempfile
from markdown.markdown_builder import MarkdownBuilder
from markdown.list import *
from markdown.table import Row, Table

@pytest.fixture
def md():
    return MarkdownBuilder("test")

# TODO: Add tests for MarkdownBuilder
def test_empty_markdown(md: MarkdownBuilder):
    assert len(md.elements) == 0

def test_add_header(md: MarkdownBuilder):
    md.addHeader(level=1, text="Test Header")
    assert len(md.elements) == 1

def test_add_unordered_lists(md: MarkdownBuilder):
    uol = UnorderedList(["test"])
    md.addUnorderedList(uol)
    assert len(md.elements) == 1

def test_add_ordered_lists(md: MarkdownBuilder):
    uol = OrderedList(["test"])
    md.addOrderedList(uol)
    assert len(md.elements) == 1

def test_add_checkbox_lists(md: MarkdownBuilder):
    uol = CheckboxList(["test"])
    md.addCheckboxList(uol)
    assert len(md.elements) == 1

def test_add_table(md: MarkdownBuilder):
    rows = [Row(["1", "2", "3"]), Row(["one","two","three"])]
    md.addTable(Table(rows))
    assert len(md.elements) == 1

def test_toStr_no_elements(md: MarkdownBuilder):
    assert not md.toStr()

def test_toStr_with_elements(md: MarkdownBuilder):
    text = "Test Header"
    md.addHeader(level=1, text=text)
    assert md.toStr() == f"# {text}"

def test_write(md: MarkdownBuilder):
    # No error should be thrown if path is written to successfully
    path = "/dev/null"
    md.write(path)
    assert True
    
