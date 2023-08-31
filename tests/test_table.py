import pytest

from markdown.table import Row, Table, TableAlign


def test_row():
    cells = ["1", "2", "3"]
    row = Row(cells)
    assert len(row.cells) == len(cells)
    assert row.md_str() == "|1|2|3|"


def test_empty_table():
    table = Table()
    assert not len(table.rows)

def test_table_header_alignment():
    headerRow = Row(["1", "2", "3"])
    inputs = [
        [TableAlign.CENTER, "|1|2|3|\n|:---:|:---:|:---:|"],
        [TableAlign.LEFT, "|1|2|3|\n|:---|:---|:---|"],
        [TableAlign.RIGHT, "|1|2|3|\n|---:|---:|---:|"],
    ]
    for input in inputs:
        align, expected = input
        table = Table(rows=[headerRow], align=align)
        assert table.md_str() == expected

def test_table_add_row():
    headerRow = Row(["1", "2", "3"])
    expected = "|1|2|3|\n|:---|:---|:---|\n|one|two|three|"

    table = Table(rows =[headerRow])
    table.addRow(Row(["one","two","three"]))

    assert table.md_str() == expected