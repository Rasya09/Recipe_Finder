from Models.database import Database

class RecipeModel:
    def __init__(self):
        self.db = Database()
        self.db.connect()

    def create_recipe(self, name, ingredients, cooking_time, category, diet_type, steps, language="en"):
        query = """
        INSERT INTO recipes (name, ingredients, cooking_time, category, diet_type, steps, language)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.db.execute_query(query, (name, ingredients, cooking_time, category, diet_type, steps, language))

    def get_recipes(self):
        query = "SELECT * FROM recipes"
        result = self.db.execute_query(query)
        return result.fetchall() if result else []

    def close(self):
        self.db.close()
