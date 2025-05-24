from collections import Counter

# BasicMath.py


def calculate_mean(numbers):
    """Calculate the mean of a list of numbers."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """Calculate the median of a list of numbers."""
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    """Calculate the mode of a list of numbers."""
    if not numbers:
        return None
    frequency = Counter(numbers)
    max_count = max(frequency.values())
    modes = [key for key, count in frequency.items() if count == max_count]
    if len(modes) == len(numbers):
        return None  # No mode if all numbers appear only once
    return modes if len(modes) > 1 else modes[0]