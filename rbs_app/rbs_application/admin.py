from django.contrib import admin
from .models import *

# Register your models here.

myModels = [UserProfile, Rating, Category, Product, Order, Complaint, ShoppingCart, Comment]  # iterable list
admin.site.register(myModels)
