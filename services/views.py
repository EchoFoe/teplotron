from django.shortcuts import render, get_object_or_404
from .models import Service
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect


def service_detail(request, id, slug):
    services = Service.objects.filter(available=True)
    service = get_object_or_404(Service, id=id, slug=slug, available=True)
    return render(request, 'services/service_detail.html', {'service': service,
                                                            'services': services,
                                                            })


def service_menu(request, id, slug):
    services = Service.objects.filter(available=True)
    service = get_object_or_404(Service, id=id, slug=slug, available=True)
    return render(request, 'navbar/navbar.html', {'service': service,
                                                  'services': services,
                                                  })


def service_footer(request, id, slug):
    services = Service.objects.filter(available=True)
    service = get_object_or_404(Service, id=id, slug=slug, available=True)
    return render(request, 'footer/footer.html', {'service': service,
                                                  'services': services,
                                                  })
