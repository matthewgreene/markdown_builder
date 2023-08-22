import pytest
from markdown.elements import Header
text = "Test text"

def test_valid_headers():
    testcases = [
        [1, f"# {text}"],
        [2, f"## {text}"],
        [3, f"### {text}"],
        [4, f"#### {text}"],
        [5, f"##### {text}"],
        [6, f"###### {text}"],
    ]
    for case in testcases:
        level, expected = case
        actual = Header(level=level, text=text)
        assert actual.md_str() == expected

def test_invalid_headers():
    levels = [0, 7]
    for level in levels:
        with pytest.raises(ValueError) as err:
            Header(level=level, text=text)
        assert str(err.value) == "Header level should be between 1 and 6"