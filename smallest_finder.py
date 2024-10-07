# smallest_finder.py

def find_two_smallest(numbers):
    """Return the two smallest numbers in a list."""
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    
    smallest = float('inf')
    second_smallest = float('inf')
    
    for number in numbers:
        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif smallest < number < second_smallest:
            second_smallest = number
            
    return smallest, second_smallest