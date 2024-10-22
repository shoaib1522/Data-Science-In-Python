
## Python Programming Concepts - Assignment 3

## Overview

This project contains solutions for **Assignment 3** of Python programming, which covers:
1. **E-commerce Data Processing**: Using lambda functions, `filter()`, `map()`, `reduce()`, and exception handling.
2. **Iterators and Generators**: Creating a custom iterator and a generator function.
3. **Exception Handling and Decorators**: Implementing chained exceptions and a decorator for logging exceptions.

The code is organized into separate tasks as required in the assignment.

---

## Task 1: E-commerce Data Processing

### Part A: Data Validation
- Filters out invalid orders where the total is non-numeric or less than zero.
- Implements a lambda function and `filter()` with proper exception handling.

### Part B: Discount Application
- Applies a 10% discount on orders where the total is above $300 using the `map()` function.

### Part C: Total Sales Calculation
- Calculates the total sales after applying discounts using `reduce()`.

---

## Task 2: Iterators and Generators

### Part A: Custom Iterator
- Implements a custom iterator called `SquareIterator`, which yields the squares of the first `n` natural numbers.

### Part B: Fibonacci Generator
- Defines a generator function `fibonacci_generator()` that yields the Fibonacci sequence up to a given number `n`.

---

## Task 3: Exception Handling and Function Decorators

### Part A: Chained Exceptions
- Divides a list of numbers by a divisor, raising a custom exception for division by zero.
- Raises appropriate exceptions for other errors (like non-numeric inputs) and chains them to the custom exception.

### Part B: Exception Logging Decorator
- Creates a decorator that logs any exceptions raised during the execution of a function.

---


## Technologies Used

- **Python 3.x**
- **Jupyter Notebook** (for testing the code)
- Python's built-in functions (`filter()`, `map()`, `reduce()`)
- Custom iterators and generators

---
