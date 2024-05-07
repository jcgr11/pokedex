import pymysql
import db_config_file


def connect_to_database() -> pymysql.connections.Connection:
    try:
        return pymysql.connect(
            host=db_config_file.DB_SERVER,
            user=db_config_file.DB_USER,
            password=db_config_file.DB_PASS,
            database=db_config_file.DB,
            cursorclass=pymysql.cursors.DictCursor,
        )
    except pymysql.Error as error:
        raise ConnectionError(f"Error connecting to MySQL: {error}")


def load_pokemon() -> list:
    with connect_to_database() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    "SELECT PokemonID, Name, Height, Weight, Description FROM Pokemon"
                )
                return cursor.fetchall()
            except pymysql.Error as e:
                raise RuntimeError(f"Error loading pokemon: {e}")


def add_pokemon(name: str, height: float, weight: float, description: str):
    with connect_to_database() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    "INSERT INTO Pokemon (Name, Height, Weight, Description) VALUES (%s, %s, %s, %s)",
                    (name, height, weight, description),
                )
                conn.commit()
            except pymysql.Error as e:
                raise RuntimeError(f"Error adding pokemon: {e}")


def register_user(username, password):
    try:
        with connect_to_database() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"INSERT INTO User (Username, Password) VALUES (%s, %s)",
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
