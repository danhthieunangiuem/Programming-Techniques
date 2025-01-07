import random

def is_perfect_number(n):
    if n <= 0:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def initialize_list():
    return [random.randint(-100, 100) for _ in range(10)]

def add_element(lst, element):
    lst.append(element)

def count_occurrences(lst, k):
    return lst.count(k)

def sum_of_perfect_numbers(lst):
    return sum(num for num in lst if is_perfect_number(num))

def sort_ascending(lst):
    return sorted(lst)

def sort_descending(lst):
    return sorted(lst, reverse=True)

def delete_element(lst, element):
    if element in lst:
        lst.remove(element)

def delete_negative_numbers(lst):
    return [num for num in lst if num >= 0]


def clear_list(lst):
    lst.clear()

def main():
    # Initialize list
    my_list = initialize_list()
    print("Initial List:", my_list)

    # Add elements
    add_element(my_list, int(input("Enter an element to add: ")))
    print("List after adding an element:", my_list)

    # Count occurrences of k
    k = int(input("Enter a number (k) to count occurrences: "))
    print(f"Number {k} appears {count_occurrences(my_list, k)} times.")

    # Sum of perfect numbers
    print("Sum of perfect numbers in the list:", sum_of_perfect_numbers(my_list))

    # Sort ascending and descending
    print("List sorted in ascending order:", sort_ascending(my_list))
    print("List sorted in descending order:", sort_descending(my_list))

    # Delete an element
    element_to_delete = int(input("Enter an element to delete: "))
    delete_element(my_list, element_to_delete)
    print("List after deleting an element:", my_list)

    # Delete negative numbers
    my_list = delete_negative_numbers(my_list)
    print("List after deleting negative numbers:", my_list)

    # Clear the entire list
    clear_list(my_list)
    print("List after clearing all elements:", my_list)
main()
