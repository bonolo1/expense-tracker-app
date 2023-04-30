from django.db import models
import datetime
from datetime import datetime

# Create your models here.
#Ref source for assistance with this: https://www.youtube.com/watch?v=cWq6jQGWmEg&t=737s
EXPENSE_CATEGORY = [
    ('EDUCATION', 'Education'),
    ('ENTERTAINMENT', 'Entertainment'),
    ('PERSONAL CARE', 'Personal Care'),
    ('FOOD_&_DINING', 'Food & Dining'),
    ('CLOTHING', 'Clothing'),
    ('GIFTS_DONATIONS', 'Gifts & Donations'),
    ('UTILITIES', 'Utilities'),
    ('TRANSPORT', 'Transport'),
    ('INVESTMENTS', 'Investments'),
    ('SAVINGS', 'Savings'),
    ('TRAVEL', 'Travel'),
    ('FEES_CHARGES', 'Fees & Charges'),
    ('TAXES', 'Taxes'),
    ('HOUSING', 'Housing'),
    ('HEALTHCARE', 'Healthcare'),
    ('MISCHELLANEOUS', 'Miscellaneous')
]
    
class Expense(models.Model):
    date = models.DateField()
    item_description = models.CharField(max_length=100)
    category_descr = models.CharField(max_length=50, choices=EXPENSE_CATEGORY)
    expense_amount = models.DecimalField(decimal_places=2, max_digits=9, default=0)

    def __str__(self):
        return self.item_description