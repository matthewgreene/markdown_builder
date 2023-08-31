from markdown.list import CheckboxList, Marker, OrderedList, UnorderedList
import pytest


padding = "    "

def test_unordered_lists():
    items = ["one", "two", UnorderedList(["four", "five"]), "three"]
    inputs = [
        [Marker.ASTERISK,   f"* one\n* two\n{padding}- four\n{padding}- five\n* three"],
        [Marker.DASH,       f"- one\n- two\n{padding}- four\n{padding}- five\n- three"], 
        [Marker.PLUS,       f"+ one\n+ two\n{padding}- four\n{padding}- five\n+ three"],
    ]

    for input in inputs:
        marker, expected = input
        assert UnorderedList(items=items, marker=marker).md_str() == expected

def test_add_item():
    inputs = [
        ["two", f"- one\n- two"],
        [UnorderedList(["two"]), f"- one\n{padding}- two"]
    ]
    
    for input in inputs:
        uol = UnorderedList(["one"])
        item, expected = input
        uol.add(item)
        assert uol.md_str() == expected

def test_add_invalid_item():
    invalidItem = 2
    with pytest.raises(ValueError) as err:
        uol = UnorderedList(["one"])
        uol.add(invalidItem)
    assert str(err.value) == f"Invalid item type. Expected ['str', 'BaseList']. Received {type(invalidItem)}"

def test_invalid_unordered_lists_markers():
    items = ["one", "two", "three"]
    markers = [Marker.CHECKBOX, Marker.NUMBER]

    for marker in markers:
        with pytest.raises(ValueError) as err:
            UnorderedList(items=items, marker=marker)
        assert str(err.value) == f"Invalid marker: Allowed ['*', '-', '+'], recieved [{marker.value}]"

def test_invalid_item_type():
    invalidItem = 2
    items = ["one", invalidItem, "three"]
    with pytest.raises(ValueError) as err:
        UnorderedList(items=items)
    assert str(err.value) == f"Invalid item type. Expected ['str', 'BaseList']. Received {type(invalidItem)}"

def test_ordered_lists():
    items = ["one", "two", OrderedList(["four", "five"]), "three"]
    expected = f"1. one\n1. two\n{padding}1. four\n{padding}1. five\n1. three"
    
    assert OrderedList(items).md_str() == expected

def test_checkbox_lists():
    items = ["one", "two", CheckboxList(["four", "five"]), "three"]
    expected = f"- [ ] one\n- [ ] two\n{padding}- [ ] four\n{padding}- [ ] five\n- [ ] three"
    
    assert CheckboxList(items).md_str() == expected