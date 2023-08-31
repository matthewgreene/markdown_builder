import pytest

from markdown.helper import Emphasis

def test_emphesis():
    text = "test"
    inputs = [
        ['b',  f"**{text}**"],
        ['i',  f"*{text}*"],
        ['bi', f"***{text}***"],
        ['ib', f"***{text}***"],
        ['ab', f"**{text}**"],
        ['ba', f"**{text}**"],
        ['ia', f"*{text}*"],

    ]
    for input in inputs:
        codes, expected = input
    assert Emphasis.withEnphesis(text=text, codes=codes) == expected