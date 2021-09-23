from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}


def get_total_ingredients(ingredients, count):
    total_ingredients = {}
    if ingredients is not None:
        for key in ingredients:
            total_ingredients[key] = count * ingredients[key]
    return total_ingredients


def recipe_view(request, recipe):
    count = int(request.GET.get('servings', 1))
    total_ingredients = get_total_ingredients(DATA.get(recipe), count)
    context = {'recipe': total_ingredients}
    return render(request, 'app/index.html', context)


def home_view(request):
    response = """<br>Чтобы узнать рецепт, используйте шаблон /Название/?servings=Количество
               <br>Если параметр servings не указан, то расчет приводится на одну персону
               <br>Например, /pasta/?servings=2"""

    return HttpResponse(response)
