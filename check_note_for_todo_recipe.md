# check_note_for_todo Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_note_for_todo(note):
    """
    Paramaters: 
        note: str representing a note
    Return:
        boolean: True if note contains substring '#TODO', else False
    Side effects:
        N/A
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
Given a non-string input
Returns TypeError
"""
def test_non_string_input_returns_type_error():
    expected = 'Input must be a string'
    with pytest.raises(TypeError) as e:
        check_note_for_todo(567)
    actual = str(e.value)
    assert actual == expected

"""
Given a string input containing the substring '#TODO'
Returns True
"""
def test_returns_true_if_input_contains_todo():
    assert check_note_for_todo("#TODO walk the dog")
    assert check_note_for_todo("buy milk #TODO")
    assert check_note_for_todo("Don't forget #TODO go to doctors!")

"""
Given a string input not containing the substring #TODO
Returns False
"""
def test_returns_false_if_input_does_not_contain_todo():
    assert not check_note_for_todo("walk the dog")
    assert not check_note_for_todo("buy milk")
    assert not check_note_for_todo("Don't forget go to doctors!")
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
