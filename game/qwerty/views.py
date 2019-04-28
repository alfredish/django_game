from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .forms import Form


def index(request):
'''Главная функция'''
    url = "https://translate.yandex.ru/?lang=ru-en&text={}"
    r = requests.get(url)
    var = BeautifulSoup(r.text)


    if(request.method == 'POST'):
        form = Form(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]

            context = {
                'var': var,
                'form': form,
                'name': name,
            }

            return render(request,'index.html',context)
    else:
        form = Form()

        context = {
            "var":var,
            'form':form,
        }

        return render(request,'index.html',context)
