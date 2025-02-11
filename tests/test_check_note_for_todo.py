import pytest
from lib.check_note_for_todo import check_note_for_todo

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