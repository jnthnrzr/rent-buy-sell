# Create your views here.
import decimal
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from .forms import AddWithdrawForm, UserForm, SellForm, SearchForm, ComplaintForm, RegistrationForm
from .models import UserProfile, Product, Category
# Create your views here.


def register(request):
    '''signup page view'''
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        user_form = UserForm(data=request.POST)
        # registration_form = RegistrationForm(data=request.POST)
        if user_form.is_valid(): # and registration_form.is_valid():
            user = User.objects.create_user(
                first_name=user_form.cleaned_data['first_name'],
                last_name=user_form.cleaned_data['last_name'],
                username=user_form.cleaned_data['username'],
                email=user_form.cleaned_data['email'],
                password=user_form.cleaned_data['password'],
                )
            user.save()

            # userprofile = UserProfile.objects.get_or_create(
            #     first_name=registration_form.cleaned_data['first_name'],
            #     last_name=registration_form.cleaned_data['last_name'],
            #     city=registration_form.cleaned_data['city'],
            #     country=registration_form.cleaned_data['country']
            # )
            # userprofile.save()

            registered = True

        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors)
    else:
        # Not a HTTP POST, so we render our form using the ModelForm instance.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        # registration_form = RegistrationForm()
        # profile_form = UserProfileForm()
    # Render the template depending on the context.
    return render(request, 'registration.html',
                  {'user_form': user_form,
                   # 'registration_form': registration_form,
                   'registered': registered})


def redir(request):
    '''TODO redirection for top nav bar'''
    return redirect('/rbs')

@login_required
def add_withdraw(request):
    profile = UserProfile.objects.get(user=request.user)
    add_withdraw_form = AddWithdrawForm(request.POST)
    if request.method == 'POST':
        if request.POST['add']:
            add = decimal.Decimal(request.POST['add'])
            profile.balance += add
            profile.save()
        if request.POST['withdraw']:
            withdraw = decimal.Decimal(request.POST['withdraw'])
            profile.balance -= withdraw
            profile.save()
        return HttpResponseRedirect(reverse('user'))
    else:
        return render(request, 'add_withdraw.html',
                      {'add_withdraw_form': add_withdraw_form,
                       'username': request.user.username,
                       'money': profile.balance})


@login_required
def cart(request):
    return render(request, 'cart.html', )

@login_required
def confirm_checkout(request):
    return render(request, 'confirm_checkout.html')

@login_required
def edit_listings(request):
    return render(request, 'edit_listings.html')


def file_complaint(request):
    complaint_form = ComplaintForm(request.POST)
    context_dict = {
        'complaint-form': complaint_form,
        'process_complaint': '/rbs/submitted-complaint',
        'user':request.user.username
    }
    return render(request, 'file_complaint.html', context_dict)


def process_complaint(request):
    '''
    *** Put the functions to process complaints and send them to db here - same method as the others
    do request.POST['name value in template'] to access values
    :param request:
    :return:
    '''
    context_dict = {
        'user': request.user.username,

    }
    print (request.POST)
    if request.POST['reported_user'] or request.POST['complaint'] == "" or " ":
        return HttpResponseRedirect('complaint')


    return render(request,'complaint_submitted.html',context_dict)

@login_required
def sell_item(request):
    '''
    :param request:
    :return:
    has the sell form, sends the return values to process the request at function process_sell()
    '''

    sell_form = SellForm(request.POST)
    context_dict = {
        'sell_form': sell_form,
        'process_sell_post': '/rbs/process-listing'
    }
    return render(request, 'sell_item.html',context_dict)

@login_required
def process_sell(request):
    context_dict = {
        'user': request.user.username,
    }
    """
    have the functions for search processing in here
    to access the values in the SellForm, do request.POST['name value in template']
    """
    print (request.POST) # just for checking the values returned in terminal
    # if fields are blank redirect back to refill the form
    if (request.POST['item'] or request.POST['price'] or request.POST['daymonth']or request.POST['time'] or request.POST['description']) == None:
        print("invalid entry ")
        return HttpResponseRedirect('sell')

    # create the Product entry
    c = Category()
    c.save()
    product = Product(seller=request.user,
                      title = request.POST['item'],
                      text = request.POST['description'],
                      takedown_date = request.POST['daymonth'],
                      takedown_time = request.POST['time'],
                      category = c,
                      price = request.POST['price'],
                      # TODO Change status to a boolean field, Charfield will make it harder to tell what is an active listing
                      # Maybe even change its name to is_active_listing
                      # Also maybe get rid of categories?
                      )
    product.save()
    return render(request, 'sell_processed.html')


def show_results(request):
    search_form = request.GET['search_input']
    if 'rent_option' in request:
        rent_option = request.GET['rent_option']
    else:
        rent_option = 'off'
    if 'buy_option' in request:
        buy_option = request.GET['buy_option']
    else:
        buy_option = 'off'
    if 'auction_option' in request:
        auction_option = request.GET['auction_option/']
    else:
        auction_option = 'off'
    min_price = request.GET['minprice']
    if min_price == '':
        min_price = 0
    max_price = request.GET['maxprice/']
    if max_price == '':
        max_price = 99999.99
    print(search_form, rent_option, buy_option, auction_option, min_price, max_price)
    if search_form == '':
        products = Product.objects.all()
        context = {'products': products}
        template = 'results.html'
        print(context)
        return render(request, template, context)
    products = Product.objects.all()
    context = {'products': products}
    template = 'results.html'
    x = Product.objects.get(title=search_form)
    if Product.objects.get(title=search_form):
        products = Product.objects.all()
        searched_context = Product.objects.get(title=search_form)
        result_c =[]
        result_c.append(searched_context) # add the searched Product into the list, the template will access the title
        # context dict to store all the values passed into the param
        context_dict = {'title': "Search Results",
                        'results': result_c,
                        'found': True, # need to set this to true or nothing will show
                        }
        if request.method == "POST":
            print("######## got to this part ")
            return render(request, 'user_item_details.html')
        
        return render(request, template, context_dict)
    # needs catch statement if product.objects.get != search form...
    '''
    write ur model lookup stuff here and return the stuff you find. Check the results template for the values you need to return per item
    '''
    # -------- getting to item details page

    return render(request, template, context)


@login_required
def buy_item_details_users(request):
    profile = UserProfile.objects.get(user=request.user)
    context_dict = {
        'user' : request.user.username,
        'money' : profile.balance,

    }
    return render(request,'user_item_details.html',context_dict)


@login_required
def update_account(request):
    return render(request, 'update_info.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect(reverse('user'))
            else:
                # Return a 'disabled account' error message
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the blank dictionary object...
        return render(request, 'login.html', {})

@login_required
def user_main(request):
    profile = UserProfile.objects.get(user=request.user)
    context_dict={
        'username': request.user.username,
        'money': profile.balance,
    }
    print ( "####### ", profile.balance)
    if request.user.is_authenticated:
        if profile.verified_by_admin == True:
            print(profile.verified_by_admin)
            return render(request, 'user_main.html', context_dict)
        else:
            return HttpResponse("You have not been verified by an admin")

@login_required
def view_previous_orders(request):
    # Render the page for previous orders
    return render(request, 'previous_orders.html')


def visitors_main(request):
    # Redirect to visitor home page
    return render(request, 'visitors_main.html')


# @login_required
def user_logout(request):
    logout(request)
    # Redirect to visitor home page
    return HttpResponseRedirect(reverse('visitor'))
