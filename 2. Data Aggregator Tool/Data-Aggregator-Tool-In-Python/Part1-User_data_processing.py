# List of user data (user_id, user_name, age, country)
users = [
    (1, 'Alice', 32, 'USA'),
    (2, 'Bob', 27, 'Canada'),
    (3, 'Charlie', 35, 'USA'),
    (4, 'David', 22, 'Mexico'),
    (5, 'Alice', 36, 'Canada'),
]

# Filter users older than 30 from 'USA' and 'Canada'
def filter_users(users):
    result = []
    for user in users:
        if user[2] > 30 and (user[3] == 'USA' or user[3] == 'Canada'):
            result.append(user[1])  # Add user name to result
    return result

# Sort users by age and return the top 10 oldest
def get_top_oldest_users(users):
    users_sorted = sorted(users, key=lambda x: x[2], reverse=True)
    return users_sorted[:10]

# Find duplicate names in the list
def find_duplicates(users):
    seen_names = set()
    duplicates = set()
    for user in users:
        if user[1] in seen_names:
            duplicates.add(user[1])
        seen_names.add(user[1])
    return list(duplicates)

# Testing the functions
print("Filtered Users:", filter_users(users))
print("Top 10 Oldest Users:", get_top_oldest_users(users))
print("Duplicate Names:", find_duplicates(users))
