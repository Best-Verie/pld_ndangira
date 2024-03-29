
class User:
    """User object with all properties of a user in the system"""
    id = None
    username = None
    email = None
    password = None

    first_name = None
    last_name = None
    nationality = None
    phone = None
    address = None
    gender = None
    user_type = None
    created_at = None
    updated_at = None

    def __str__(self):
        """String representation of the User object with all properties"""
        return ("User(id='%s', username='%s', password='%s', email='%s', first_name='%s', last_name='%s')" %
                (self.id, self.username, self.password, self.email, self.first_name, self.last_name))