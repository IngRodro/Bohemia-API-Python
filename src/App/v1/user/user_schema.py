def user_entity(user) -> dict:
    return {
        'id': str(user['_id']),
        'name': user['name'],
        'password': user['password'],
        'username': user['username'],
        'status': user['status'],
    }

def users_entity(entity) -> list:
    return [user_entity(item) for item in entity]