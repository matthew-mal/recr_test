from django.contrib import admin
from django.urls import path
from echo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello, name='hello')
]
