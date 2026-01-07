from evaluation.numeric_utils import extract_numbers

def numeric_faithfulness(answer, context_chunks):
    """
    Ensures numeric values in the answer are supported by retrieved context.
    Returns a structured metric dictionary.
    """
    answer_nums = extract_numbers(answer)
    context_nums = []

    for c in context_chunks:
        context_nums.extend(extract_numbers(c))

    if not answer_nums:
        # No numbers to verify → considered faithful
        return 1.0 # no numbers -->Fully faithful

    matched = sum(1 for num in answer_nums if num in context_nums)
    return matched / len(answer_nums) # Return ratio of matched numbers