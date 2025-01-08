def calculate_statistics(numbers):
     count = len(numbers)
     total = sum(numbers)
     mean = total / count
     maxValue = max(numbers)
     minValue = min(numbers)
     return count, total, mean, maxValue, minValue

input_list = input("Nhập các số cách nhau bằng dấu cách: ")
numbers = list(map(int, input_list.split()))

stats = calculate_statistics(numbers)
print('(count, total, mean, maxValue, minValue) =',stats)
(count, total, mean, maxValue, minValue) = stats
print(f"count={count}")
print(f"total={count}")
print(f"average={mean}")
print(f"maxValue={maxValue}")
print(f"minValue={minValue}")