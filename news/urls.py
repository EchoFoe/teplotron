from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:id>/<slug:slug>/', views.news_detail, name='news_detail'),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
