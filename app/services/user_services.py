
def serialize_user(user):
    return {
        'id': user.id,
        'name': user.name,
        'description': user.description,
        'email': user.email,
        'user_type': user.user_type,
        'created_at': user.create_at
    }


def serialize_user_list(user_list):
    return [serialize_user(user) for user in user_list]
