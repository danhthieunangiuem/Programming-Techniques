def has_symmetric(set_of_tuples):
    checked = set()
    for tpl in set_of_tuples:
        if (tpl[1], tpl[0]) in checked:  # Check if the reverse exists in the set
            return True
        checked.add(tpl)
    return False

# Example Usage
set_of_tuples = {(1, 2), (2, 1), (3, 4), (4, 3), (5, 6)}
result = has_symmetric(set_of_tuples)
print("Contains Symmetric Tuples:", result)
