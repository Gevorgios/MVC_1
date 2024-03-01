# # Model
# class Shoe:
#     def __init__(self, shoe_type, shoe_style, color, price, manufacturer, size):
#         self.shoe_type = shoe_type
#         self.shoe_style = shoe_style
#         self.color = color
#         self.price = price
#         self.manufacturer = manufacturer
#         self.size = size
#
# # View
# class ShowView:
#     def show_shoe_details(self, shoe):
#         print("Shoe details:")
#         print(f"Type: {shoe.shoe_type}")
#         print(f"Style: {shoe.shoe_style}")
#         print(f"Color: {shoe.color}")
#         print(f"Price: {shoe.price}")
#         print(f"Manufacturer: {shoe.manufacturer}")
#         print(f"Size: {shoe.size}")
#
# # Controller
# class ShoeController:
#     def __init__(self, shoe):
#         self.shoe = shoe
#         self.view = ShowView()
#
#     def show_shoe_details(self):
#         self.view.show_shoe_details(self.shoe)
#
# shoe = Shoe("Men's", "Sneakers", "Black", 50, "Nike", 10)
# controller = ShoeController(shoe)
# controller.show_shoe_details()


# 2


# class Recipe:
#     def __init__(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
#         self.name = name
#         self.author = author
#         self.recipe_type = recipe_type
#         self.description = description
#         self.video_link = video_link
#         self.ingredients = ingredients
#         self.cuisine = cuisine
#
# class RecipeView:
#     def show_recipe_details(self, recipe):
#         print("Recipe Details:")
#         print(f"Name: {recipe.name}")
#         print(f"Author: {recipe.author}")
#         print(f"Type: {recipe.recipe_type}")
#         print(f"Description: {recipe.description}")
#         print(f"Video Link: {recipe.video_link}")
#         print(f"Ingredients")
#         for ingredient in recipe.ingredients:
#             print(f"- {ingredient}")
#         print(f"Cuisine: {recipe.cuisine}")
#
# class RecipeController:
#     def __init__(self, recipe):
#         self.recipe = recipe
#         self.view = RecipeView()
#
#     def show_recipe_details(self):
#         self.view.show_recipe_details(self.recipe)
#
#
# ingredients = ["Tomatoes", "Basil", "Mozzarella", "Olive oil"]
# recipe = Recipe("Caprese Salad", "Italian Chef", "Appetizer", "A simple and delicious italian salad", "https://www.youtube.com/watch?v=12345", ingredients, "Italian")
# controller = RecipeController(recipe)
# controller.show_recipe_details()



