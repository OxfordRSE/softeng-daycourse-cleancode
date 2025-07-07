import sys
from pathlib import Path
from smoothie import smoothie
sys.path.append(str(Path(__file__).parent.parent / "src"))


def test_smoothie():
    assert smoothie(["banana", "strawberry", "yogurt"]) == "Icy Water smoothie with banana, strawberry, yogurt"
    ...  # Continue adding tests here
