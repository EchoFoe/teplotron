from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from services.models import Service
from reviews.models import Comment
from news.models import New
from about_us.models import AboutUs, AboutUsDetails, Partners


def home(request):
    services = Service.objects.filter(available=True)
    about_us = AboutUs.objects.filter(available=True)
    partners = Partners.objects.filter(available=True)
    reviews = Comment.objects.filter(available=True)
    news = New.objects.filter(available=True)
    return render(request, 'home/home.html', {'services': services,
                                              'about_us': about_us,
                                              'partners': partners,
                                              'reviews': reviews,
                                              'news': news,
                                              })


def service_detail(request, id, slug):
    services = Service.objects.filter(available=True)
    service = get_object_or_404(Service, id=id, slug=slug, available=True)
    about_us = AboutUs.objects.filter(available=True)
    return render(request, 'services/service_detail.html', {'service': service,
                                                            'services': services,
                                                            'about_us': about_us,
                                                            })
