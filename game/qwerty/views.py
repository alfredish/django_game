from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .forms import Form


def index(request):

    if(request.method == 'POST'):
        form = Form(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]

            #укажите свой ключ https://translate.yandex.ru/developers/keys ссылка на получение ключа
            key = ""
            url = "https://translate.yandex.net/api/v1.5/tr/translate?key=" + key + "&text=" + str(name) + "&lang=en-ru"

            r = requests.get(url)

            var = BeautifulSoup(r.text)
            var = var.findAll("text")
            var = var[0].string

            context = {
                'var': var,
                'form': form,
                'var': var,
            }

            return render(request,'index.html',context)
    else:
        form = Form()

        context = {
            'form' : form,
        }

        return render(request,'index.html',context)
