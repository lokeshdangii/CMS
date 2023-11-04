# concept of context processor

from flask import session

def usernames():
    # Define variables you want to make available globally
    variables = {
        'username': session.get('username', None),
        'role': session.get('role', None)  # Fetch and make the 'role' available
    }
    # print(variables)
    return variables






