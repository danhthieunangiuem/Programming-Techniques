numbers_list = [(1, 2, 3, 4), (5, 13, 7, 8), (9, 10, 11, 12)]
sumAll = 0  # Total sum across all tuples

for t in numbers_list:
    print(t)
    sumt = 0  # Sum for the current tuple

    # Use enumerate to get both index and value
    for index, v in enumerate(t):
        if index % 2 == 1 and v % 2 == 0:  # Odd index and even value
            sumt += v

    print(f"Sum of t = {sumt}")
    sumAll += sumt  # Add current tuple sum to total sum

print(f"Sum all = {sumAll}")
