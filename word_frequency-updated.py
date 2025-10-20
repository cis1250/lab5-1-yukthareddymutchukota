#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

# Get and validate the sentence input.
def get_sentence():
   
    while True:

        # Prompt the user: Ask the user to enter a sentence.
        user_sentence = input("Enter a sentence: ")

        if is_sentence(user_sentence):
            return user_sentence
        
        else:
            print("This does not meet the criteria for a sentence.\n")


# Calculate word frequencies. 
def calculate_frequencies(sentence):
    
    # Split the sentence.
    words = sentence.split()

    # Create lists to store words and their corresponding frequencies.
    unique_words = []
    frequencies = []

    # Iterate through words and update frequencies.
    for word in words:
        
        # Removes punctuation and makes all words lowercase.
        word = word.strip(".,!?").lower()

        # If the word is in unique_words, find all indexes of the word and add one to it's position in the frequencies list each time.
        if word in unique_words:
            index = unique_words.index(word)
            frequencies[index] += 1
        
        # If the word is not in unique_words, add it to the list and update frequency of word to 1.
        else:
            unique_words.append(word)
            frequencies.append(1)

    return unique_words, frequencies


# Print frequencies.
def print_frequencies(words, frequencies):
    print("\nWord Frequencies:")
    
    # For the number of words in unique_words / For the length of the list unique_words, print word with it's designated frequency.
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")


# Run code / main ()
words, frequencies = calculate_frequencies(get_sentence())
print_frequencies(words, frequencies)
