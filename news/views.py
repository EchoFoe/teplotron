from django.shortcuts import render, get_object_or_404
from .models import New
from services.models import Service
from about_us.models import AboutUs
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect


def news_detail(request, id, slug):
    services = Service.objects.filter(available=True)
    news = New.objects.filter(available=True)
    new = get_object_or_404(New, id=id, slug=slug, available=True)
    about_us = AboutUs.objects.filter(available=True)
    return render(request, 'news/news_detail.html', {'new': new,
                                                     'news': news,
                                                     'services': services,
                                                     'about_us': about_us,
                                                     })


def news_list(request):
    services = Service.objects.filter(available=True)
    about_us = AboutUs.objects.filter(available=True)
    news = New.objects.filter(available=True)
    return render(request, 'news/news_list.html', {'about_us': about_us,
                                                   'services': services,
                                                   'news': news,
                                                   })
