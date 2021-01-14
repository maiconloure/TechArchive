
def serialize_user(user):
    return {
        'id': user.id,
        'name': user.name,
        'description': user.description,
        'email': user.email,
        'created_at': user.create_at if f'{user.create_at}' != 'null' else ' '
    }


def serialize_user_list(user_list):
    return [serialize_user(user) for user in user_list]
