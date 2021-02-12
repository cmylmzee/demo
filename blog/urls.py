from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    path('', views.index, name='anasayfa' ),
    path('blog', views.blog, name='hakkımda' ),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)