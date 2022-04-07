from xmlrpc.client import DateTime
from django.db import models
from django.utils import timezone
from house.models import House
from django.core.validators import MinValueValidator


class Expenses(models.Model):
    class Category(models.TextChoices):
        RENT = 'Rent'
        MORTGAGE = 'Mortgage'
        BILLS = 'Bills'
        TRANSPORTATION = 'Transportation'
        CLOTHING = 'Clothing'
        HEALTHCARE = 'Healthcare'
        FOOD = 'Food'
        INSURANCE = 'Insurance'
        KIDS = 'Kids'
        CULTURE = 'Culture'
        VACATIONS = 'Vacations'
        OTHER = 'Other'

    description = models.TextField(max_length=250, default='')
    category = models.CharField(max_length=32, choices=Category.choices, default=Category.OTHER)
    house_name = models.ForeignKey(House, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    date = models.DateTimeField(timezone.now())

    def __str__(self):
        return f'Category:{self.category},Amount:{self.amount}'

    def get_expense_by_house(self, house):
        return Expenses.objects.filter(house_name=house)

    @staticmethod
    def create_expense(house_name: House, amount: int, date: DateTime, category: Category, description=""):
        expense = Expenses(house_name=house_name, amount=amount, date=date, category=category, description=description)
        expense.save()
        return expense
