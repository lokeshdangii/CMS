# concept of context processor

from flask import session

def usernames():
    # Define variables you want to make available globally
    variables = {
        'username': session.get('username', None)
    }
    return variables



