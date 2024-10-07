# main.py

from smallest_finder import find_two_smallest
from integer_lists import list1, list2, list3, list4

# Define a list of lists to iterate over
lists_to_check = [list1, list2, list3, list4]

# Open the result file to write
with open("result.txt", "w") as result_file:
    for lst in lists_to_check:
        smallest_values = find_two_smallest(lst)
        result_file.write(f"The two smallest values in {lst} are: {smallest_values}\n")