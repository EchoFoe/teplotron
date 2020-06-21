from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('news/', include('news.urls', namespace='news')),
    path('about_us/', include('about_us.urls', namespace='about_us')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('summernote/', include('django_summernote.urls')),
    # path('', include('about_us.urls', namespace='about_us')),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
