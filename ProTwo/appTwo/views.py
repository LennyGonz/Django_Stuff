from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_me':'Fuck you pay me'}
    return render(request,'appTwo/index.html',context=my_dict)

def help(request):
    help = {'help_insert': 'HELP-PAGE NIGGA!'}
    return render(request,'appTwo/help.html',context = help)
