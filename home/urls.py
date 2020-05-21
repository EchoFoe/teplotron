from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/<slug:slug>/', views.service_detail, name='service_detail'),

]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
