from django.shortcuts import render

from .models import Food

def top5(request):
    """
    List of the top 5 food items.
    """
    all_food_items = Food.objects.order_by('-score')
    top5_food_items = all_food_items[:5]
    return render(request,
        'food/top5.html',
        {'top5': top5_food_items}
    )
