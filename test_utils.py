# These lines ensure that utils.py can be imported from a sibling folder
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "src"))

# Import functions from utils.py
from utils import add, is_even, to_uppercase, get_list_average


def test_add():
    assert add(1, 1) == 2
    # Add extra test cases here


def test_is_even():
    is_even(3) is True  # This test is incorrect; why doesn't it fail?
    # Add extra test cases here


def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    # Add extra test cases here


def test_get_list_average():
    assert get_list_average([1, 2, 3]) == 2.0
    # Add extra test cases here
