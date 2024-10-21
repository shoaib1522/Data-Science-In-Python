# List of transaction data (transaction_id, user_id, amount)
transactions = [
    (101, 1, 150.0),
    (102, 2, 200.0),
    (103, 3, 300.0),
    (104, 1, 250.0),
]

# Count unique users from the transactions
def count_unique_users(transactions):
    unique_users = set()
    for transaction in transactions:
        unique_users.add(transaction[1])
    return len(unique_users)

# Find the transaction with the highest amount
def find_highest_transaction(transactions):
    highest = transactions[0]
    for transaction in transactions:
        if transaction[2] > highest[2]:
            highest = transaction
    return highest

# Extract lists of transaction_ids and user_ids
def separate_ids(transactions):
    transaction_ids = []
    user_ids = []
    for transaction in transactions:
        transaction_ids.append(transaction[0])
        user_ids.append(transaction[1])
    return transaction_ids, user_ids

# Testing the functions
print("Unique User Count:", count_unique_users(transactions))
print("Highest Transaction:", find_highest_transaction(transactions))
print("Transaction and User IDs:", separate_ids(transactions))
