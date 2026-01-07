import re

def extract_numbers(text):
    """
    Extracts numeric values (ints, floats, percentages) from text.
    """
    if not text:
        return []

    numbers = re.findall(r"-?\d+\.?\d*", text)
    return numbers
