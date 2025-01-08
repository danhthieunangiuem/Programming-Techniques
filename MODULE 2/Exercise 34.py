def is_prime(num):
    'Check if a number is prime'
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input array
n = int(input("Enter the number of elements in the array: "))
array = []

print("Enter the elements of the array:")
for i in range(n):
    while True:
        try:
            element = int(input(f"Element {i + 1}: "))
            if element < 0:
                print("Please enter a natural number (non-negative integer).")
                continue
            array.append(element)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

odd_numbers = [num for num in array if num % 2 != 0]
print(f"Odd numbers: {odd_numbers}, Count: {len(odd_numbers)}")
even_numbers = [num for num in array if num % 2 == 0]
print(f"Even numbers: {even_numbers}, Count: {len(even_numbers)}")
prime_numbers = [num for num in array if is_prime(num)]
print(f"Prime numbers: {prime_numbers}")
non_prime_numbers = [num for num in array if not is_prime(num)]
print(f"Non-prime numbers: {non_prime_numbers}")
array_without_even = [num for num in array if num % 2 != 0]
print(f"Array after removing even numbers: {array_without_even}")
