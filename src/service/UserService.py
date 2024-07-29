from src.configuration.sql.Configuration import MySQL

class UserService:
    def __init__(self):
        self.self = self


def get_all_users():
    try:
        with MySQL.cursor() as db:
            db.execute('SELECT * FROM users')
            results = db.fetchall()
            columns = [desc[0] for desc in db.description]
            users = [dict(zip(columns, row)) for row in results]
        return users
    except Exception as e:
        raise Exception("Error retrieving users: " + str(e))
    finally:
        if db:
            db.close()