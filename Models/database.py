from mysql.connector import Error
import mysql.connector

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="recipe_finder"
            )
            self.cursor = self.connection.cursor(buffered=True)
        except mysql.connector.Error as e:
            print(f"Error saat menghubungkan ke database: {e}")

    def execute_query(self, query, params=None):
        if not self.cursor:
            raise AttributeError("Database cursor belum diinisialisasi. Pastikan metode connect() sudah dipanggil.")
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            if query.strip().lower().startswith("select"):
                return self.cursor  # Kembalikan cursor untuk SELECT queries
            else:
                self.connection.commit()
                return None  # Untuk query INSERT/UPDATE/DELETE
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
