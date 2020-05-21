from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import AboutUs, AboutUsDetails, Customer
from reviews.models import Comment
from services.models import Service
from experts.models import Expert
from .forms import *
from utils.emails import SendingEmail


def about(request):
    services = Service.objects.filter(available=True)
    about_us = AboutUs.objects.filter(available=True)
    comments = Comment.objects.filter(available=True)
    reviews = Service.objects.filter(available=True)
    experts = Expert.objects.filter(available=True)
    return render(request, 'about_us/about_us.html', {'about_us': about_us,
                                                      'comments': comments,
                                                      'reviews': reviews,
                                                      'services': services,
                                                      'experts': experts,
                                                      })


def about_menu(request):
    about_us = AboutUs.objects.filter(available=True)
    return render(request, 'navbar/navbar.html', {'about_us': about_us,
                                                  })


def about_footer(request):
    about_us = AboutUs.objects.filter(available=True)
    return render(request, 'footer/footer.html', {'about_us': about_us,
                                                  })


def contact(request):
    services = Service.objects.filter(available=True)
    about_us = AboutUs.objects.filter(available=True)
    form = CustomerForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        print('yes')
        data = form.cleaned_data
        print(form.cleaned_data['email'])
        # new_form = form.save()
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        message = data.get('message')
        email = data.get('email')
        phone = data.get('phone')

        # user, created = User.objects.get_or_create(username=phone, defaults={"first_name": first_name, "email": email})
        order = Customer.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone, message=message)
        # order = Sportsman.objects.update()

        email = SendingEmail()
        email.sending_email(type_id=1, order=order)
        email.sending_email(type_id=2, email=order.email, order=order)
        return render(request, 'thanks/thanks.html', locals())
    else:
        form = CustomerForm()
    return render(request, 'contacts/contacts.html', locals())
