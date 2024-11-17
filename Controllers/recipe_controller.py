from Models.recipe_model import RecipeModel

class RecipeController:
    def __init__(self):
        self.model = RecipeModel()

    def add_recipe(self):
        name = input("Nama Resep: ")
        ingredients = input("Bahan (pisahkan dengan koma): ")
        cooking_time = int(input("Waktu Memasak (menit): "))
        category = input("Kategori: ")
        diet_type = input("Jenis Diet: ")
        steps = input("Langkah-langkah: ")

        self.model.create_recipe(name, ingredients, cooking_time, category, diet_type, steps)
        print("Resep berhasil ditambahkan!")

    def list_recipes(self):
        recipes = self.model.get_recipes()
        for recipe in recipes:
            print(f"{recipe[0]}: {recipe[1]} (Kategori: {recipe[4]})")
