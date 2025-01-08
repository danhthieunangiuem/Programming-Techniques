def analyze_string(input_string):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    numbers = list(map(int, input_string.split(';')))

    # Output digits on separate lines
    print("Digits on Separate Lines:")
    for num in numbers:
        print(num)

    # Even digit statistics
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("\nEven Numbers:", even_numbers)
    print("Even Count:", len(even_numbers))

    # Negative digit statistics
    negative_numbers = [num for num in numbers if num < 0]
    print("\nNegative Numbers:", negative_numbers)
    print("Negative Count:", len(negative_numbers))

    # Prime digit statistics
    prime_numbers = [num for num in numbers if is_prime(num)]
    print("\nPrime Numbers:", prime_numbers)
    print("Prime Count:", len(prime_numbers))

    # Average value
    avg_value = sum(numbers) / len(numbers)
    print("\nAverage Value:", round(avg_value, 2))

def main():
    input_string = input("Enter a string of numbers separated by ';' (e.g., 5;7;8;-2;8;11;13;9;10): ")
    analyze_string(input_string)
main()
