from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord #connecting to the database
# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date') # order_by is a sequel command that simply sorts by whatever, in this case database
    date_dict = {'access_records':webpages_list} #template tag

    my_dict = {'insert_me':"Hello I am from first_app/index.html ! "}
    return render(request,'first_app/index.html',context=date_dict)
