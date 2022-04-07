from django.http import HttpResponse
from house.models import Country, House, City
from expenses.models import Expenses
from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone


def home_page(request):
    return render(request, "home.html")


def global_page(request):
    country = Country.objects.get(name="Israel")
    house = House.create_house(
        'House 1',
        True,
        Country.objects.get(name="Israel"),
        City.objects.get(name="Tel Aviv", country=country),
        'Teacher',
        'Teacher',
        100,
        1,
    )

    Expenses.create_expense(
        house_name=house, amount='2500', date=timezone.now(), category='Rent', description="description"
    )

    all_houses = House.objects.all()
    categories_amounts = Expenses.objects.order_by().values('category').annotate(total=Sum("amount"))

    context = {
        'all_houses': all_houses,
        "categories": [category.get('category') for category in categories_amounts],
        "amounts": [amount.get('total') for amount in categories_amounts],
    }
    return render(request, 'global.html', context)


def house_login(request):
    return HttpResponse('house login')


def house_view(request, house_id):
    return HttpResponse(f'this is the house view for house {house_id}')


def add_house(request):
    post = request.POST["id"]
    return HttpResponse(f"try to update data for house POST PARAMETERS {'None' if post is None else post}")
