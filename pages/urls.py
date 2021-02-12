from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='a' ),
    path('about', views.about, name='b' ),
    path('hakkımda', views.hakkımda, name='b' ),

]