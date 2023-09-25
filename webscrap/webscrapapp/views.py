from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import ScrapLink

def home(request):
    if request.method == 'POST':
        url_input = request.POST.get('urlInput')
        scrap_web = requests.get(url_input)
        bs = BeautifulSoup(scrap_web.text, 'html.parser')
        ScrapLink.objects.all().delete()
        for i in bs.find_all('a'):
            link_address = i.get('href')
            link_name = i.string
            ScrapLink.objects.create(address=link_address, string_name=link_name)
    data_values = ScrapLink.objects.all()
    return render(request, 'home.html', {'data': data_values})
