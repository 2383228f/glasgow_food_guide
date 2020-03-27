from django.shortcuts import render

# Create your views here.
def index(request):
   
    
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    
    response = render(request, 'food/index.html', context=context_dict)
    return response