import bcrypt
from Models.user_model import UserModel

class UserController:
    def __init__(self):
        self.model = UserModel()

    def register(self):
        """Mendaftarkan pengguna baru."""
        print("\n=== Register ===")
        username = input("Masukkan Username: ")
        
        # Validasi password
        while True:
            password = input("Masukkan Password (minimal 8 karakter): ")
            if len(password) >= 8:
                break
            print("Password harus memiliki minimal 8 karakter!")
        
        # Pilih role menggunakan angka
        while True:
            print("\nPilih Role:")
            print("1: Chef")
            print("2: User")
            role_choice = input("Masukkan pilihan (1/2): ")
            
            if role_choice == "1":
                role = "chef"
                break
            elif role_choice == "2":
                role = "user"
                break
            else:
                print("Pilihan tidak valid! Masukkan 1 atau 2.")
        
        # Cek apakah username sudah ada
        existing_user = self.model.get_user_by_username(username)
        if existing_user:
            print("Username sudah digunakan. Silakan pilih username lain.")
            return

        # Simpan ke database
        try:
            self.model.create_user(username, password, role)
            print("Registrasi berhasil!")
        except Exception as e:
            print(f"Error saat registrasi: {e}")

    def login(self):
        """Login pengguna"""
        print("\n=== Login ===")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        # Ambil data user dari database
        user = self.model.get_user_by_username(username)
        if user:
            # Verifikasi password yang di-hash dengan input password
            if bcrypt.checkpw(password.encode('utf-8'), user[2].encode('utf-8')):  # user[2] adalah hashed password
                print("Login berhasil!")
                role = user[3]  # user[3] adalah kolom role
                from Views.main_menu import post_login_menu
                post_login_menu(role, username)  # Kirim username ke menu utama
            else:
                print("Password salah!")
        else:
            print("Username tidak ditemukan.")

