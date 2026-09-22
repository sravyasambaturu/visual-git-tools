def calculate_total(items):
    """Return the sum of all item prices."""
    total = 0
    for price in items:
        total += price
    return total