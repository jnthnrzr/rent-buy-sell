from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import Product, ShoppingCart, UserProfile
from ..date_checker import update_all
from django.db.models import Sum

@login_required
def cart(request):
    """Buttons handled: ADD TO CART, REMOVE FROM CART

    Renders: cart.html
    """
    update_all()
    profile = UserProfile.objects.get(user=request.user)
    context_dict = {
        'username': request.user.username,
        'money': profile.balance,
    }
    cart = ShoppingCart.objects.get_or_create(user=profile)[0]
    # Check if "ADD ITEM TO CART" was pressed
    if 'add_to_cart' in request.POST:
        product_pk = request.POST['add_to_cart']
        product = Product.objects.get(pk=product_pk)
        print("\n\n",profile.user, product.seller, str(profile.user)==str(product.seller),"\n\n")
        if  str(profile.user) == str(product.seller):
            context_dict['messages'] = "You cannot buy your own items!"
            return render(request, 'badAction.html', context_dict)
        print("\n\n ADD TO CART was pressed for product_pk: \n\n", product_pk)
        cart.products.add(product)
        cart_total = cart.products.all().aggregate(Sum('price'))
        cart.totalPrice = cart_total['price__sum']
        print("++++++++++++++++++ CART TOTAL IS:", cart.totalPrice)
        # cart.totalPrice=float(cart.products.all().aggregate(Sum('price'))['price__sum'])
        cart.save()
        context_dict['products'] = cart.products.all()
        context_dict['totalPrice'] = cart.totalPrice
        return render(request, 'cart.html', context_dict)

    # Check if "REMOVE" was pressed
    elif 'remove' in request.POST:
        # Find which product was added to cart
        product_pk = request.POST['remove']
        product = Product.objects.get(pk=product_pk)
        print('REMOVE button was pressed for product_pk:', product)
        cart.products.remove(product)
        cart.save()
    # Display the Cart Page
    # cart = ShoppingCart.objects.get_or_create(user=profile)[0]
    # context_dict['cart.pk'] = cart.pk
    context_dict['products'] = cart.products.all()
    print("\n\n\n",cart.totalPrice,"\n\n")
    context_dict['totalPrice'] = cart.totalPrice
    return render(request, 'cart.html', context_dict)
