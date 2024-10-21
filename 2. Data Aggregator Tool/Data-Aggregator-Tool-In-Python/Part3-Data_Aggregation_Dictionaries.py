# Dictionary of user feedback (user_id: {'rating': int, 'comments': str})
feedback = {
    1: {'rating': 5, 'comments': 'Great!'},
    2: {'rating': 4, 'comments': 'Good job!'},
    3: {'rating': 2, 'comments': 'Needs improvement.'},
    4: {'rating': 5, 'comments': 'Excellent!'},
}

# Filter users with rating 4 or higher
def high_rated_users(feedback):
    high_rated = {}
    for user_id, data in feedback.items():
        if data['rating'] >= 4:
            high_rated[user_id] = data['rating']
    return high_rated

# Get top 5 users by rating (sorted in descending order)
def top_rated_users(feedback):
    sorted_users = sorted(feedback.items(), key=lambda x: x[1]['rating'], reverse=True)
    return dict(sorted_users[:5])

# Testing the functions
print("High Rated Users:", high_rated_users(feedback))
print("Top Rated Users:", top_rated_users(feedback))
