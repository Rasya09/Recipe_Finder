from Models.database import Database

class ReviewModel:
    def __init__(self):
        self.db = Database()
        self.db.connect()

    def create_review(self, recipe_id, user_id, rating, review_text):
        query = """
        INSERT INTO reviews (recipe_id, user_id, rating, review_text)
        VALUES (%s, %s, %s, %s)
        """
        self.db.execute_query(query, (recipe_id, user_id, rating, review_text))

    def get_reviews(self, recipe_id):
        query = """
        SELECT r.review_text, r.rating, u.username
        FROM reviews r
        JOIN users u ON r.user_id = u.id
        WHERE r.recipe_id = %s
        """
        reviews = self.db.execute_query(query, (recipe_id,))
        reviews = reviews.fetchall() if reviews else []

        avg_rating_query = "SELECT AVG(rating) AS avg_rating FROM reviews WHERE recipe_id = %s"
        avg_rating = self.db.execute_query(avg_rating_query, (recipe_id,))
        avg_rating = avg_rating.fetchone()["avg_rating"] if avg_rating else None

        return reviews, avg_rating

    def close(self):
        self.db.close()
