from Controllers.user_controller import UserController
from Controllers.recipe_controller import RecipeController
from Controllers.review_controller import ReviewController  # Tambahan untuk ulasan


def main_menu():
    user_controller = UserController()
    recipe_controller = RecipeController()
    review_controller = ReviewController()  # Instance untuk ulasan
    logged_in_user = None

    while True:
        print("===== Recipe Finder ===== \n")
        if not logged_in_user:
            print("1. Register")
            print("2. Login")
        else:
            print("1. Tambah Resep")
            print("2. Lihat Daftar Resep")
            print("3. Tambahkan Ulasan")
            print("4. Lihat Ulasan Resep")
            print("5. Logout")
        print("0. Keluar")
        print("\n ===== Recipe Finder ===== \n")
        choice = input("Pilih opsi: ")

        if choice == "1":
            if not logged_in_user:
                user_controller.register()
            else:
                recipe_controller.add_recipe()
        elif choice == "2":
            if not logged_in_user:
                logged_in_user = user_controller.login()
            else:
                recipe_controller.list_recipes()
        elif choice == "3" and logged_in_user:
            add_review(review_controller, logged_in_user["id"])
        elif choice == "4" and logged_in_user:
            view_reviews(review_controller)
        elif choice == "5" and logged_in_user:
            print("Logout berhasil.")
            logged_in_user = None
        elif choice == "0":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")


def add_review(review_controller, user_id):
    """Tambahkan ulasan untuk resep."""
    try:
        recipe_id = int(input("Masukkan ID resep yang ingin diulas: "))
        rating = int(input("Masukkan penilaian (1-5): "))
        if rating < 1 or rating > 5:
            print("Penilaian harus antara 1 dan 5!")
            return
        review_text = input("Masukkan ulasan Anda: ")
        review_controller.add_review(recipe_id, user_id, rating, review_text)
        print("Ulasan berhasil ditambahkan!")
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk ID resep dan penilaian.")


def view_reviews(review_controller):
    """Lihat ulasan untuk resep tertentu."""
    try:
        recipe_id = int(input("Masukkan ID resep untuk melihat ulasan: "))
        reviews, avg_rating = review_controller.view_reviews(recipe_id)
        print(f"\n===== Ulasan untuk Resep ID {recipe_id} =====")
        if reviews:
            for review in reviews:
                print(f"{review['username']} memberi {review['rating']} bintang: {review['review_text']}")
            print(f"Rata-rata rating: {avg_rating:.1f}")
        else:
            print("Belum ada ulasan untuk resep ini.")
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk ID resep.")


def post_login_menu(role, username):
    from datetime import datetime

    # Tentukan salam berdasarkan waktu
    hour = datetime.now().hour
    if 5 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    # Tampilkan salam dan username
    print("\n====================================")
    print(f"Welcome {username}, {greeting}!")
    print("====================================")

    # Tampilkan menu utama
    print("\n=== Menu Utama ===")
    if role == "chef":
        print("1. Tambahkan Resep")
        print("2. Lihat Resep")
        print("3. Ubah Resep")
        print("4. Hapus Resep")
    elif role == "user":
        print("1. Cari Resep")
        print("2. Filter Resep")
        print("3. Favoritkan Resep")
        print("4. Lihat Resep Favorit")

    print("0. Keluar")
    pilihan = input("Pilih opsi: ")
    handle_post_login_menu(pilihan, role, username)


def handle_post_login_menu(pilihan, role, username):
    if role == "chef":
        if pilihan == "1":
            print("Tambahkan Resep - Fitur belum diimplementasikan.")
        elif pilihan == "2":
            print("Lihat Resep - Fitur belum diimplementasikan.")
        elif pilihan == "3":
            print("Ubah Resep - Fitur belum diimplementasikan.")
        elif pilihan == "4":
            print("Hapus Resep - Fitur belum diimplementasikan.")
        elif pilihan == "0":
            print("Keluar dari menu utama.")
            return
        else:
            print("Pilihan tidak valid!")
    elif role == "user":
        if pilihan == "1":
            print("Cari Resep - Fitur belum diimplementasikan.")
        elif pilihan == "2":
            print("Filter Resep - Fitur belum diimplementasikan.")
        elif pilihan == "3":
            print("Favoritkan Resep - Fitur belum diimplementasikan.")
        elif pilihan == "4":
            print("Lihat Resep Favorit - Fitur belum diimplementasikan.")
        elif pilihan == "0":
            print("Keluar dari menu utama.")
            return
        else:
            print("Pilihan tidak valid!")

    # Tampilkan menu kembali setelah operasi selesai
    post_login_menu(role, username)
