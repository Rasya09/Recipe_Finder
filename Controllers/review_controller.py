from Models.review_model import ReviewModel

class ReviewController:
    def __init__(self):
        self.review_model = ReviewModel()

    def add_review(self, user_id):
        recipe_id = input("Masukkan ID resep: ")
        rating = int(input("Masukkan penilaian (1-5): "))
        review_text = input("Masukkan ulasan: ")

        self.review_model.create_review(recipe_id, user_id, rating, review_text)
        print("Ulasan berhasil ditambahkan.")

    def view_reviews(self, recipe_id):
        reviews, avg_rating = self.review_model.get_reviews(recipe_id)
        print(f"Ulasan untuk Resep ID {recipe_id}:")
        for review in reviews:
            print(f"{review['username']} memberi {review['rating']} bintang: {review['review_text']}")
        print(f"Rata-rata rating: {avg_rating}")
