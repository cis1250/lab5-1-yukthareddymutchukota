# Lab 5 

# Part 1: Fibonacci Sequence with functions

## Objective
Create a Python program that calculates and prints the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence) up to a specified number of terms. 
Unlike the previous version of this lab, you will structure your program using **functions** to demonstrate the **principle of modularity**.

---

## Requirements

1. **Use functions**  
   - Your program must use three functions:
     - One for **validating and returning user input**.
     - One for **generating the Fibonacci sequence**.
     - One for **printing the sequence**.

2. **Prompt the user**
   - Use the `input()` function to ask the user how many terms of the Fibonacci sequence they want. 

3. **Validate the input**
   - Ensure the user enters a **positive integer**.
   - If the input is invalid, display an error message and prompt again.

4. **Generate the Fibonacci sequence**
   - Use a **for loop** to generate the sequence up to the specified number of terms.
   - Return the sequence as a list.

5. **Print the result**
   - Display the Fibonacci sequence in a readable format.

---
# Part 2: Word Frequency with functions

## Objective
Write a Python program that takes a sentence as input and calculates the frequency of each word in the sentence using **functions** and **modular programming principles**.

---

## Requirements


1. **Use functions**
   - Your program should be organized into **at least three functions**:
      - `get_sentence()` — to get and validate the sentence input.  
      - `calculate_frequencies(sentence)` — to calculate word frequencies.  
      - `print_frequencies(words, frequencies)` — to display the results.
   - A `main()` function should control the overall program flow.
     
2. **Prompt the user**
   - Use the `input()` function to ask the user to enter a sentence. (Note that in the word_frequency.py file a function is provided to check if the input is a sentence. A sentence starts with a capital letter, contains at least one word and ends with a punctuation mark (period, question mark, exclamation mark).)
  
3. **Split the sentence into words**
   - Split the input sentence into a list of words using the [split()](https://docs.python.org/3/library/stdtypes.html#str.split) method.
  
4. **Create lists**
   - Create two empty lists to store words and their corresponding frequencies.
  
5. **Iterate through words and update frequencies**
   - Iterate through the list of words.
   - Check for existence: Check if the word is already in the list of words.
   - Update frequency: If the word exists, update its frequency in the corresponding list. Otherwise, append both the word and a frequency of 1 to the lists.
  
6. **Print results**
   - Print the word frequencies in a readable format.
