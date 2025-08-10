from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from businessdata import views

def test_view(request):
    return HttpResponse("Test view working!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view, name='test'),
    path('', views.business_list, name='business_list'),
    path('add/', views.add_business, name='add_business'),
]
