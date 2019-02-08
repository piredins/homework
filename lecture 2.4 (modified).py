def dictionary_making():
  cook_book = {}
  with open('cookbook.txt', encoding='utf8') as recipes:
    for line in recipes:
      l = 0
      ingredients_list = []
      ingredients = []
      key = line.strip()
      i = recipes.readline()
      while l < int(i):
        ingredient = recipes.readline().strip()
        ingredient = ingredient.split('|')
        ingredients.append(ingredient)
        l += 1
      for ingredient in ingredients:
        ingredients_dict = {
        'ingridient_name': ingredient[0],
        'quantity':ingredient[1],
        'measure':ingredient[2]
        }
        ingredients_list.append(ingredients_dict)
      recipes.readline()
      cook_book.update({key: ingredients_list})
    return cook_book

dictionary_making()
#print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
  cook_book = dictionary_making()
  shopping_list = {}
  for dish in dishes:
    if dish in cook_book.keys():
      for ingredient in cook_book.get(dish):
        quantity = int(ingredient.get('quantity')) * person_count
        measure_quantity = {
        'measure': ingredient.get('measure'),
        'quantity': quantity
        }
        shopping_list.update({ingredient.get('ingridient_name'): measure_quantity})
  print(shopping_list)
        
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 7)