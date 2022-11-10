with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dishes = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            emp = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = emp
            ingredients.append({'ingredient_name': ingredient_name,
                              'quantity': quantity,
                              'measure': measure})
        file.readline()
        cook_book.update({dishes: ingredients})

print(cook_book)
print()

def get_shop_list_by_dishes(dishes_person, person_count):
    ingredients_person = {}
    ingredients_list = {}
    for dishes, ingredients in cook_book.items():
        if dishes in dishes_person:
            ingredients_person.update({dishes: ingredients})
    for dishes, ingredients in ingredients_person.items():
        for ingredient in ingredients:
            key1 = ingredient.pop('ingredient_name')
            key2 = int(ingredient.get('quantity'))
            key3 = ingredient.popitem()
            ingredient.update({'quantity': key2 * person_count})
            ingredient.update({key3})
            ingredients_list.update({key1: ingredient})

    print(ingredients_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)