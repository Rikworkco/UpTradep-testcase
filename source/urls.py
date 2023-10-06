from django.contrib import admin
from django.urls import path
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('news', views.other),
    path('profile', views.other),
    path('reg', views.other),
    path('login', views.other),
    path('what', views.other),
    path('reset_password', views.other),
]
