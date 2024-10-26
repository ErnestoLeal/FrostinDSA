"""
URL configuration for Website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('challenges/', views.challenge_list, name='challenge_list'),

    path('admin/', admin.site.urls),
    path('', include('challenges.urls')),
    path('submit_attempt/', views.submit_attempt, name='submit_attempt')

]"""
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('challenges/', include('challenges.urls')),  # Include URLs from the challenges app
]"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Importing RedirectView for redirection
from challenges import views  # Importing the homepage view

urlpatterns = [
    #path('', RedirectView.as_view(url='', permanent=False)),  # Redirect root to challenges
    path('admin/', admin.site.urls),  # Admin URL
    path('', views.home, name='home'),  # Set the homepage at the root URL
    path('challenges/', include('challenges.urls')),  # Include challenges app URLs
    path('code_executor/', include('code_executor.urls')),
]



