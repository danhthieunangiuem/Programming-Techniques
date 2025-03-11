def find(main_set, subsets):
    largest_subset = set()
    for subset in subsets:
        if main_set.isdisjoint(subset):  # Check if there's no common element
            if len(subset) > len(largest_subset):
                largest_subset = subset  # Update if this subset is larger
    return largest_subset
# Example Usage
main_set = {1, 2, 3, 4}
subsets = [{2, 3}, {1, 2}, {5, 6}, {3, 4}]

result = find(main_set, subsets)
print("Largest Non-Overlapping Subset:", result)
