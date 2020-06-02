from django.shortcuts import render, get_object_or_404
from .models import Portfolio, PortfolioDetails
from services.models import Service
from about_us.models import AboutUs
from documentations.models import Document
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect


def portfolio_detail(request, id, slug):
    services = Service.objects.filter(available=True)
    portfolios = Portfolio.objects.filter(available=True)
    portfolio = get_object_or_404(Portfolio, id=id, slug=slug, available=True)
    about_us = AboutUs.objects.filter(available=True)
    documents = Document.objects.filter(available=True)
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio': portfolio,
                                                               'portfolios': portfolios,
                                                               'services': services,
                                                               'about_us': about_us,
                                                               'documents': documents,
                                                               })


def portfolio_list(request):
    portfolio = Portfolio.objects.filter(available=True)
    services = Service.objects.filter(available=True)
    about_us = AboutUs.objects.filter(available=True)
    portfolios = Portfolio.objects.filter(available=True)
    documents = Document.objects.filter(available=True)
    # portfolio_images = PortfolioDetails.objects.filter(available=True, portfolio__available=True)
    return render(request, 'portfolio/portfolio_list.html', {'about_us': about_us,
                                                             'services': services,
                                                             'portfolio': portfolio,
                                                             'portfolios': portfolios,
                                                             # 'portfolio_images': portfolio_images,
                                                             'documents': documents,
                                                             })
