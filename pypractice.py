# Python learning & Practice

import sys
from io import StringIO
import pytest
from unittest.mock import patch

# Input & Output 
def test_inputOutput(): 
    name = input("Enter your name")
    print("Hello", name, ",Lets start learning")

    x,y,z = input("Enter different multiple values").split()
    print(x,y,z)

    random = input("input random")
    print(random)
    print(int(random))

# Input from stdin
def test_inputstdin():
   simulated_input = "Hello\nWorld\nq\n"
    # Redirect sys.stdin to simulate user input
sys.stdin = StringIO(simulated_input)   
lines = []
for line in sys.stdin:
        if 'q' == line.rstrip():
            break
        lines.append(line.rstrip())

sys.stdin = sys.__stdin__  # Restore stdin
assert lines == ["Hello", "World"]

# Multi input from file
def test_inputFile():
    # Create a temporary file with sample content
    file = tmp_path / "sample.txt"
    file.write_text("line1\nline2\nline3\n")

    # Read file content
    with open(file, "r") as f:
        content = f.read().splitlines() 
    assert content == ["line1", "line2", "line3"]

if __name__ == "__main__":
    # Call functions
    test_inputOutput()
    test_inputstdin()
    test_inputFile()
