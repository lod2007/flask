
def format_users_forview(users):
    return [
        {
            "username": user.username,
            "email": user.email
        }
        for user in users
    ]