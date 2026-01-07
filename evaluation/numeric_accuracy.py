def numeric_accuracy(predicted, ground_truth, tolerance=0.05):
    """
    Continuous numeric accuracy score in [0, 1]
    """
    try:
        pred = float(predicted.replace("%", "").replace(",", ""))
        gold = float(ground_truth.replace("%", "").replace(",", ""))

        if gold == 0:
            return 0.0

        error_ratio = abs(pred - gold) / abs(gold)

        if error_ratio <= tolerance:
            return 1.0

        score = max(0.0, 1 - (error_ratio - tolerance))
        return round(score, 3)

    except Exception:
        return 0.0
