from django.urls import path, include
from . import views
urlpatterns = [
    path('home/', views.SchoolViewAPI.as_view(), name='home'),
    path('home/<int:pk>/', views.SchoolViewAPI.as_view(), name='home'),

]
