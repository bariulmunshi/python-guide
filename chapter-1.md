# Table of Contents
- [Basic Problem Solving Overview](#basic-problem-solving-overview)

## Basic Problem Solving Overview
1. Problem 1: Hello World 
Description: Write a Python program that prints "Hello, World!" to the console.
   ```sh
    print("Hello, World!")
  ```

2. Problem 2: Calculator
- Description:
Create a Python function calculator that takes two numbers as input and prints their sum, difference, product, and quotient.


  ```sh
    def calculator(num1, num2):
    print("Sum:", num1 + num2)
    print("Difference:", num1 - num2)
    print("Product:", num1 * num2)
    print("Quotient:", num1 / num2)
    # Example Usage:
    calculator(10, 5)
 ```
- Explanation:
The function calculator takes two parameters num1 and num2. Inside the function, it performs basic arithmetic operations and prints the results.

3. Problem 3: Even or Odd
- Description:
Write a Python function check_even_odd that checks whether a given number is even or odd.

- ```sh
  def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

    # Example Usage:
    check_even_odd(7)

  ```
-  Explanation:
The function check_even_odd takes a number as input and uses the modulo operator to check if it's divisible by 2. If the remainder is zero, the number is even; otherwise, it's odd.
4. Problem 4: List Manipulation
- Description:
Manipulate a Python list by adding an element, removing an element, and accessing an element at a specific index.

- ```sh 
    my_list = [1, 2, 3, 4, 5]

    # Add an element
    my_list.append(6)

    # Remove an element
    my_list.remove(3)

    # Access an element
    print("Element at index 2:", my_list[2])

  ```
-  Explanation:
A list named my_list is created with some initial elements. Elements can be added using the append method, removed using the remove method, and accessed using index notation.

5. Problem 5: Palindrome Checker
- Description:
Write a Python function is_palindrome that checks if a given word is a palindrome.
- ```sh 
  def is_palindrome(word):
    reversed_word = word[::-1]
    if word.lower() == reversed_word.lower():
        print("Palindrome")
    else:
        print("Not a Palindrome")

    # Example Usage:
    is_palindrome("level")

  ```
- Explanation:
The function is_palindrome takes a word as input, reverses it, and compares it with the original word. If they are the same (ignoring case), the word is a palindrome.

6. Problem 6: File Handling
- Description:
Read the content of a file named 'input.txt,' count the number of words, and write the word count to another file named 'output.txt.'
- ```sh
     # Assuming a file named 'input.txt' exists with some content
     with open('input.txt', 'r') as file:
        data = file.read()
        word_count = len(data.split())

     # Writing the word count to another file
     with open('output.txt', 'w') as output_file:
        output_file.write(f"Word Count: {word_count}")
  ```
- Explanation:
File handling is done using the open function. The with statement ensures proper file closure. The word count is obtained by reading the content of 'input.txt' and splitting it into words.

7. Problem 7: Prime Number Generator
- Description:
Write a Python function generate_primes that generates a list of prime numbers up to a specified limit.
- ```sh 
        def generate_primes(limit):
            primes = []
            for num in range(2, limit + 1):
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)
            return primes

        # Example Usage:
        limit = 50
        prime_numbers = generate_primes(limit)
        print(f"Prime numbers up to {limit}: {prime_numbers}")

  ```

- Explanation:
The function uses the Sieve of Eratosthenes algorithm, iterating through numbers up to the given limit and checking for divisibility. Prime numbers are added to the primes list, which is then returned.

Feel free to run these code snippets to see the results and experiment with variations!