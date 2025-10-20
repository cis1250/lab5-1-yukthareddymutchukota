#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# Validate that the input is a positive integer. ✓
# TODO: (Read detailed instructions in the Readme file) 
#!/usr/bin/env python3


# Get valid user input. 
def get_positive_integer():
    
    # Validate that the input is a positive integer. 
    while True:
        user_input = input("Enter the number of terms wanted for Fibonacci Sequence: ")
        
        # Safe to convert to integer and break.
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        
        else:
            print("Oh no! What you have entered is not a positive integer. Please try again.\n")


# Generate Fibonacci sequence.
def generate_fibonacci(num_terms):
    sequence = []

    # Initialize variables for fibonacci sequence computation.
    a, b = 0, 1

    for i in range(num_terms):
        sequence.append(a)
        a, b = b, a + b

    return sequence


# Print the sequence.
def print_fibonacci(sequence):
    print("\nFibonacci Sequence:")
    print(" ".join(str(num) for num in sequence))


# Run code / main ()
print_fibonacci(generate_fibonacci(get_positive_integer()))