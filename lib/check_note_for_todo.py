def check_note_for_todo(note):
    if not isinstance(note, str):
        raise TypeError("Input must be a string")
    return '#TODO' in note