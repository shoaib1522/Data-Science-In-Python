
#### Data Aggregator Tool in Python

## Overview

This project implements a **Smart Data Aggregator Tool** using Python, designed to efficiently manage and analyze user data. The tool focuses on working with different types of Python collections such as Lists, Tuples, Sets, and Dictionaries to handle various tasks including real-time analytics, data tracking, and reporting.

This tool was developed as part of an individual project to demonstrate Python programming skills and data handling capabilities.

## Features

The Data Aggregator Tool provides the following functionality:

### 1. **User Data Processing with Lists**
- Filters out users older than 30 from the USA and Canada.
- Extracts names of filtered users into a new list.
- Sorts user data by age and returns the top 10 oldest users.
- Checks for duplicate user names.

### 2. **Immutable Data Management with Tuples**
- Counts the total number of unique users from transaction data stored as tuples.
- Identifies the highest transaction without modifying the original data.
- Separates transaction IDs and user IDs into two separate lists.

### 3. **Unique Data Handling with Sets**
- Finds users who visited both Page A and Page B.
- Identifies users who visited either Page A or Page C, but not both.
- Updates the set for Page A with new user IDs.
- Removes a list of user IDs from the set for Page B.

### 4. **Data Aggregation with Dictionaries**
- Filters users with a rating of 4 or higher and stores their user ID and rating in a new dictionary.
- Sorts the dictionary by rating and returns the top 5 users.
- Combines feedback from multiple dictionaries, ensuring the highest rating is kept and comments are merged.
- Creates a new dictionary of user IDs and ratings for all users with a rating greater than 3 using dictionary comprehension.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/shoaib1522/Data-Aggregator-Tool-In-Python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Data-Aggregator-Tool-In-Python
   ```
3. Open the Jupyter Notebook to explore and test the functionality:
   ```bash
   jupyter notebook
   ```

## Requirements

- Python 3.x
- Jupyter Notebook
- No additional libraries are required, as the project uses only built-in Python collections and functions.

## Repository Structure

```
Data-Aggregator-Tool-In-Python/
│
├── DataAggregatorTool.ipynb   # Jupyter notebook with all implementations
|   Parts python files         # Just initial implementations
└── README.md                  # Project overview and usage guide
```

## Conclusion

This project demonstrates my ability to work with Python collections such as lists, tuples, sets, and dictionaries. The functions are designed to perform data aggregation tasks efficiently and provide real-time analytics capabilities.

Feel free to explore the code, contribute, or use it for your own projects. You can access the repository here: [Data Aggregator Tool in Python](https://github.com/shoaib1522/Data-Aggregator-Tool-In-Python).

## License

This project is open-source and available under the [MIT License](LICENSE).
