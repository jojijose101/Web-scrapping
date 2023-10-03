from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

from websapp.models import Link


# Create your views here.
def index(request):
    if request.method=="POST":
        link_page = request.POST.get('page','')
        url = requests.get(link_page)
        webs = BeautifulSoup(url.text,'html.parser')

        for link in webs.find_all('a'):
              li_adrs = link.get('href')
              li_name = link.string
              Link.objects.create(address=li_adrs,strname=li_name)
              HttpResponseRedirect('/')
    address = Link.objects.all()


    return render(request,'index.html',{'adrs':address})

def clear(request):
    link = Link.objects.all()
    link.delete()
    return redirect('/')