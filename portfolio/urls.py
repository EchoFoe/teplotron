from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('<int:id>/<slug:slug>/', views.portfolio_detail, name='portfolio_detail'),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
