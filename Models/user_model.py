import bcrypt
from Models.database import Database
import hashlib

class UserModel:
    def __init__(self):
        self.db = Database()
        self.db.connect()

    def hash_password(self, password):
        """Hash password untuk keamanan."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password, role):
        """Registrasi pengguna baru."""
        hashed_password = self.hash_password(password)
        query = """
        INSERT INTO users (username, password, role)
        VALUES (%s, %s, %s)
        """
        self.db.execute_query(query, (username, hashed_password, role))

    def get_user_by_username(self, username):
        query = "SELECT * FROM users WHERE username = %s"
        result = self.db.execute_query(query, (username,))
        return result.fetchone()
    
    def create_user(self, username, password, role):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
        try:
            self.db.execute_query(query, (username, hashed_password, role))
        except Exception as e:
            print(f"Error saat menyimpan pengguna: {e}")


    def close(self):
        self.db.close()
