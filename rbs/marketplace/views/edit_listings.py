from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..date_checker import update_all
from ..models import Product, UserProfile
from ..date_checker import update_all


@login_required
def edit_listings(request):
    update_all()
    """Edit a previous posting of a Product for sale

    A user who has listed a Product for sale earlier can remove it.
    """
    profile = UserProfile.objects.get(user=request.user)
    context_dict = {
        'username': request.user.username,
        'money': profile.balance,
    }
    update_all()
    if request.method == 'POST':
        pk = request.POST.get('remove', ' ')
        item = Product.objects.get(pk=pk)
        item.is_active = False
        item.save()
    listings = Product.objects.filter(seller=profile, is_active=True)
    context_dict['listings'] = listings
    return render(request, 'edit-listings.html', context_dict)
