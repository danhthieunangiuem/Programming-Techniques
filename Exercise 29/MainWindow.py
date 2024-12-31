def NegativeNumberInStrings(s):
    # Find all negative integers using regular expression
    negative_numbers = re.findall(r'-(\d+)', s)

    # Convert the extracted numbers to integers and add a negative sign
    negative_integers = [-int(num) for num in negative_numbers]

    # Output results
    print("Negative integers found:", negative_integers)
    print("Total count of negative integers:", len(negative_integers))