from django.shortcuts import render
from appTwo.models import User

# Create your views here.
def index(request):
    my_dict = {'insert_me':'Fuck you pay me'}
    return render(request,'appTwo/index.html',context=my_dict)

def help(request):
    help = {'help_insert': 'HELP-PAGE NIGGA!'}
    return render(request,'appTwo/help.html',context = help)

def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'appTwo/users.html', context=user_dict)


