from django.contrib import admin
from django.urls impor
from django.contrib import admin
from django.urls import path, include
from frontend.views import IndexView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(¨, )
]

