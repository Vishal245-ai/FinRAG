def finance_chunk (text: str, min_len: int = 300):
    sections = text.splt("\n\n")
    return [s.strip() for s in sections if len(s.strip()) > min_len]