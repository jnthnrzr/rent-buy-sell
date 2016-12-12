from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth.models import User
from django.shortcuts import render
from ..models import Order, ShoppingCart, UserProfile, Rating
from ..update_rating import update_rating
from ..date_checker import update_all


@login_required
def orders(request):
    # Render the page for previous orders
    profile = UserProfile.objects.get(user=request.user)
    context_dict = dict()
    update_all()
    if "confirm_checkout" in request.POST:
        cart = ShoppingCart.objects.get(user=profile)
        new_order = Order(user=profile)
        new_order.save()
        new_order.products.add(*cart.products.all())
        for product in cart.products.all():
            seller = product.seller
            seller.balance += product.price
            seller.save()
            profile.balance -= product.price
            profile.save()
            product.quantity -= 1
            if product.quantity == 0:
                product.is_active = False
                product.save()
        cart_total = cart.products.all().aggregate(Sum('price'))
        amount = cart_total['price__sum']
        print("CART TOTAL was: $", amount)
        new_order.save()
        cart.delete()
    all_orders = Order.objects.filter(user=profile)

    # Check if previous orders exist
    if all_orders.count():
        orders_list = list(all_orders.all())
        order_dic = {}
        for order in orders_list:
            product_list = list(order.products.all())
            order_dic[str(order.pk)] = product_list
        context_dict['allorders'] = order_dic

    context_dict['username'] = request.user.username
    context_dict['money'] = profile.balance
    if "rating" in request.POST:
        rating_input = request.POST['rating']
        listed_seller = request.POST.get('seller', ' ')
        user_seller = User.objects.get(username = listed_seller)
        seller_profile = UserProfile.objects.get(user = user_seller)
        new_rating = Rating(user=seller_profile,rating = int(rating_input))
        new_rating.save()
        update_rating(seller_profile)
        print ("*******", rating_input, '****', listed_seller)
    return render(request, 'orders.html', context_dict)
