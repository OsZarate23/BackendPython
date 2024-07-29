from ..Configuration import get_db_connection

connection = get_db_connection()


class UserService:
    def __init__(self):
        self.self = self


def get_all_users():
    connection = None
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            results = cursor.fetchall()
        return results
    except Exception as e:
        raise Exception("Error retrieving users: " + str(e))
    finally:
        if connection:
            connection.close()
