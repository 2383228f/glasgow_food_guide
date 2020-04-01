from django.shortcuts import render
from food.forms import UserForm, UserProfileForm, RestaurantForm, CommentForm,AddFavouriteForm
from food.models import UserProfile, Comment, Restaurant
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
import profile
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.template.defaultfilters import slugify
# Create your views here.
def index(request):
   
    
    context_dict = {}
    context_dict['boldmessage'] = 'Welcome to Glasgow Food Guide!'
    try:
        context_dict['user_profile'] = UserProfile.objects.get(username=request.user.username)
    except:
        context_dict['user_profile'] = None
    response = render(request, 'food/index.html', context=context_dict)
    return response

def register(request):
    registered = False;
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
            
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.username = user.username
            
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request, 'food/register.html', 
                  context = {'user_form':user_form,
                            'profile_form': profile_form,
                            'registered': registered})    
                
def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return redirect(reverse('food:index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'food/login.html')

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('food:index'))

def add_restaurant(request):
    form = RestaurantForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form = form.save(commit=False)
            form.owner = UserProfile.objects.get(username=request.user.username)
            form.save()
            # Now that the category is saved, we could confirm this.
            # For now, just redirect the user back to the index view.
            return redirect('/food/')
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'food/add_restaurant.html', {'form': form})

def add_comment(request, restaurant_name_slug):
    
    try:
        restaurant = Restaurant.objects.get(slug=restaurant_name_slug)
    except Restaurant.DoesNotExist:
        restaurant = None
    print(restaurant.slug)
    if restaurant is None:
        return redirect('/food/')
    form = CommentForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            print(restaurant.slug)
            if restaurant:
                # Save the new category to the database.
                form = form.save(commit=False)
                form.date_time =datetime.now()
                form.restaurant = Restaurant.objects.get(slug=restaurant_name_slug)
                form.user = UserProfile.objects.get(username=request.user.username)
                form.save()
                # Now that the category is saved, we could confirm this.
                # For now, just redirect the user back to the index view.
                return redirect(reverse('food:show_restaurant',kwargs={'restaurant_name_slug':restaurant_name_slug}))
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    context_dict = {'form': form, 'restaurant': restaurant}
    return render(request, 'food/add_comment.html', context=context_dict)


def show_restaurant(request, restaurant_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        restaurant = Restaurant.objects.get(slug=restaurant_name_slug)
        
        # Retrieve all of the associated pages.
        # The filter() will return a list of page objects or an empty list.
        comments = Comment.objects.filter(restaurant=restaurant)
        
        # Adds our results list to the template context under name pages.
        context_dict['comments'] = comments
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['restaurant'] = restaurant
    except Restaurant.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['restaurant'] = None
        context_dict['comments'] = None
        
    # Go render the response and return it to the client.
    return render(request, 'food/restaurant.html', context=context_dict)

def show_restaurants(request):
    context_dict = {}
    context_dict['restaurants']= Restaurant.objects.all()

    response = render(request, 'food/restaurants.html', context=context_dict)
    return response

def search(request):

    
    if 'text' in request.GET:
        slugged = slugify(request.GET['text'])
        restaurant = Restaurant.objects.filter(slug=slugged)
        if restaurant:
            return redirect(reverse('food:show_restaurant',kwargs={'restaurant_name_slug':slugged}))
        else:
            context_dict = {}
            context_dict['boldmessage'] = 'Please enter the restaurant name eg: Pizza Express'

            return(render(request, 'food/index.html', context=context_dict))
        
def account(request):
   
    
    context_dict = {}
    context_dict['boldmessage'] = 'Welcome to Glasgow Food Guide!'
    context_dict['user_profile'] = UserProfile.objects.get(username=request.user.username)

    response = render(request, 'food/account.html', context=context_dict)
    return response
    
    
def add_favourite(request):
    form = AddFavouriteForm()
    

    # A HTTP POST?
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(username=request.user.username)
        form = AddFavouriteForm(request.POST, instance=user_profile)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form = form.save(commit=False)
          
           

            restaurantOb = Restaurant.objects.get(slug=slugify(form.favourites))
            
            user_profile.favourites.append(restaurantOb)
            form.save()
            #form.save()
            print("working stxsill")
            # Now that the category is saved, we could confirm this.
            # For now, just redirect the user back to the index view.
            return(render(request, 'food/index.html'))
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    context_dict = {}
    context_dict['boldmessage'] = 'Welcome to Glasgow Food Guide!'
    userp = UserProfile.objects.get(username=request.user.username)
    context_dict['user_profile'] = userp
    context_dict['slugs'] = []
    for fav in userp.favourites:
        print("fav"+fav)
        context_dict['slugs'].append(slugify(fav))
    print(context_dict['slugs'])
    context_dict['form'] = form
    response = render(request, 'food/account.html', context=context_dict)
    return response

