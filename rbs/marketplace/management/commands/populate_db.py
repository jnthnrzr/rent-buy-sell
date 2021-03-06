''' Use this script to populate the datebase for rbs
    Type in: python populate_rbs.py and check the data in the admin site. '''
# from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from ...models import *


ENGINEERS = [{"username": "jonathanrozario",
              "password": "pass",
              "phone": "2126507000",
              "city": "Harlem",
              "country": "USA",
              "balance": '1234.95', },
             {"username": "cyan",
              "password": "pass",
              "phone": "2126507000",
              "city": "Harlem",
              "country": "USA",
              "balance": '1234.95', },
             {"username": "heyconnie123",
              "password": "pass",
              "phone": "2126507000",
              "city": "Harlem",
              "country": "USA",
              "balance": '1234.95', },
             {"username": "alphamale",
              "password": "pass",
              "phone": "2126507000",
              "city": "Harlem",
              "country": "USA",
              "balance": '1234.95', }, ]

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def clear_users(self):
        users = User.objects.all()
        users.delete()

    def clear_cat(self):
        cats = Category.objects.all()
        cats.delete()

    def clear_products(self):
        products = Product.objects.all()
        products.delete()

    def add_user(self, username, password):
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return user

    def createsuperuser(self):
        superuser = User.objects.create_superuser(username='rbs', email='', password='rbs')
        superuser.save()
        return superuser

    def add_userprofile(self, user, phone, city, country, balance):
        import decimal
        profile = UserProfile.objects.get_or_create(user=user)[0]
        profile.verified_by_admin = True
        profile.city = city
        profile.country = country
        profile.balance = decimal.Decimal(balance)
        profile.save()
        return profile

    # def add_cart(self, user, product):
    #     profile = UserProfile.objects.get_or_create(user=user)[0]
    #     cart = ShoppingCart.objects.get_or_create(user=profile)
    #
    #     return cart

    # def add_superuser(self, username, password):
    #     superuser = User.objects.create_superuser(username=username, password=password)
    #     superuser.save()
    #     return superuser

    def add_product(self, seller, title, price, option):
        p = Product.objects.get_or_create(seller=seller, title=title,
                                          price=price, option=option)[0]
        p.save()
        return p

    def add_cat(self, name):
        c = Category.objects.get_or_create(name=name)[0]
        c.save()
        return c

    def _populate(self):
        # First, we will create lists of dictionaries containing the Products
        # we want to add into each category.
        # Then we will create a dictionary of dictionaries for our categories.
        # This might seem a little bit confusing, but it allows us to iterate
        # through each data structure, and add the data to our models.

        clothing = [
            {"title": "Pink Chanel Suit",
             "price": 1000,
             "option": "A"},
            {"title": "Bjork's Swan Dress",
             "price": 80,
             "option": "A"},
            {"title": "Black Givenchy Dress",
             "price": 500,
             "option": "A"},
        ]

        games = [
            {"title": "Cities: Skylines",
             "price": 7.99,
             "option": "B"},
            {"title": "Counter-Strike: Global Offensive",
             "price": 10.04,
             "option": "B"},
            {"title": "The Last of Us Remastered",
             "price": 14.99,
             "option": "B"},
            {"title": "Civilization VI",
             "price": 12.99,
             "option": "B"},
            {"title": "Red Dead Redemption",
             "price": 59.99,
             "option": "B"},
            {"title": "Just Cause 3",
             "price": 44.99,
             "option": "B"},
        ]

        books = [
            {"title": "Tango with Django",
             "price": 9.99,
             "option": "R"},
            {"title": "The Annals of America",
             "price": 166.16,
             "option": "R"},
            {"title": "Holy Bible, King James Version",
             "price": 1.00,
             "option": "R"},
            {"title": "\"Surely, You\'re Joking Mr. Feynman!\"",
             "price": 8.48,
             "option": "R"},
            {"title": "The Hitchhiker's Guide to the Galaxy",
             "price": 7.19,
             "option": "R"},
            {"title": "Flask Web Development",
             "price": 34.99,
             "option": "R"},
            {"title": "The Art of Programming",
             "price": 99.50,
             "option": "R"},
            {"title": "Harry Potter and the Cursed Child",
             "price": 13.99,
             "option": "R"},
            {"title": "Three Men on a Boat",
             "price": 4.99,
             "option": "R"},
            {"title": "Harry Potter and the Sorcerer's Stone",
             "price": 10.99,
             "option": "R"},
            {"title": "Harry Potter and the Chamber of Secrets",
             "price": 10.01,
             "option": "R"},
            {"title": "Harry Potter and the Prisoner of Azkaban",
             "price": 10.09,
             "option": "R"},
            {"title": "Harry Potter and the Goblet of Fire",
             "price": 10.15,
             "option": "R"},
            {"title": "Harry Potter and the Order of the Phoenix",
             "price": 10.99,
             "option": "R"},
            {"title": "Harry Potter and the Half-Blood Prince",
             "price": 10.99,
             "option": "R"},
            {"title": "Harry Potter and the Deathly Hallows",
             "price": 12.99,
             "option": "R"},
        ]

        sellers = [
            {"username": "nathan",
             "password": "qwerty"},
            {"username": "betam4le",
             "password": "password"},
            {"username": "yoyodog",
             "password": "easypass1234"},
            {"username": "jroz",
             "password": "fasdfcvafs"},
            {"username": "kwest",
             "password": "phasr12"},
            {"username": "hotdoglover",
             "password": "momspafehti"},
            {"username": "arioman",
             "password": "tw35243"},
            {"username": "facebooksurfer",
             "password": "mont4r"},
            {"username": "heybuddy",
             "password": "eass1234"},
            {"username": "jozie",
             "password": "fundingneeded"},
        ]

        # Dictionary of categories
        # If you want to add more categories or products, add them to the dictionaries below.
        cats = {"Clothing": {"products": clothing},
                "Games": {"products": games},
                "Books": {"products": books}}

        # Dictionary of users
        # users = {"Sellers": {"role": sellers},
        #          "superusers": {"role": superusers},}


        # for role, person in users.items():
        #     for p in person["role"]:
        #         self.add_user(p["username"], p["password"])


        # def add_superusers(self):

        for engineer in ENGINEERS:
            user = self.add_user(engineer["username"], engineer["password"], )
            self.add_userprofile(user, engineer["phone"], engineer["city"],
                                 engineer["country"], engineer["balance"], )


        # TODO this works correctly, need a better way to do it.
        # for s in sellers:
        #     s = self.add_user(s["username"], s["password"])
        #     for cat, cat_data in cats.items():
        #         c = self.add_cat(cat)
        #         for product in cat_data["products"]:
        #             self.add_product(c, s, product["title"], product["price"])

        # List of SELLER PROFILES
        open_sellers = []

        for s in sellers:
            user = self.add_user(s["username"], s["password"])
            seller = self.add_userprofile(
                user, "2126507000", "New York", "USA", 100.99)
            open_sellers.append(seller)

        # products = books + clothing + games
        # for seller, product in zip(open_sellers, products):
        #     self.add_product(seller, product["title"], product["price"],
        #                      product["option"])
        #     open_sellers.remove(seller)

        for cat, cat_data in cats.items():
            category = self.add_cat(cat)
            for seller, product in zip(open_sellers, cat_data["products"]):
                self.add_product(seller, product["title"], product["price"],
                                 product["option"])
                open_sellers.remove(seller)

                # print(open_sellers)


    def handle(self, *args, **options):
        print("Starting RBS database population...")
        print("Deleting all users...")
        self.clear_users()
        print("Deleting all categories...")
        self.clear_cat()
        print("Deleting all products...")
        self.clear_products()
        print("Making superuser: { 'USERNAME' : 'rbs', 'PASSWORD': 'rbs' ...")
        self.createsuperuser()
        print("Filling in database...")
        self._populate()
