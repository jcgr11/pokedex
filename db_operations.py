import pymysql


def connect_to_database():
    return pymysql.connect(
        host="localhost",
        user="username",
        password="password",
        database="pokedex",
        cursorclass=pymysql.cursors.DictCursor,
    )


def load_pokemon():
    try:
        with connect_to_database() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT PokemonID, Name, Height, Weight, Description FROM Pokemon"
                )
                results = cursor.fetchall()
        return results
    except pymysql.Error as e:
        print(f"Error loading pokemon: {e}")
        return []


def add_pokemon(name, height, weight, description):
    try:
        with connect_to_database() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Pokemon (Name, Height, Weight, Description) VALUES (%s, %s, %s, %s)",
                    (name, float(height), float(weight), description),
                )
                connection.commit()
    except pymysql.Error as e:
        print(f"Error adding pokemon: {e}")


def register_user(username, password):
    try:
        with connect_to_database() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO User (Username, Password) VALUES (%s, %s)",
                    (username, password),
                )
                connection.commit()
    except pymysql.Error as e:
        print(f"Error registering user: {e}")


def check_user(username, password):
    try:
        with connect_to_database() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM User WHERE Username = %s AND Password = %s",
                    (username, password),
                )
                result = cursor.fetchone()
        return result
    except pymysql.Error as e:
        print(f"Error checking user: {e}")
        return None
