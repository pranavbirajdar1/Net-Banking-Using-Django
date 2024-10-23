"""
URL configuration for dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import path,include


urlpatterns = [
    
    
    path('admin/', admin.site.urls),
     path('', include('index.urls')),
    path('userdashboar/', include('userdash.urls')),
    path('account/', include('accounts.urls')),
    path('investme/', include('investments.urls')),
    path('fundtrans/', include('fundtransfer.urls')),
    path('payme/', include('payments.urls')),
    path('settin/', include('settings.urls')),
    path('statement/', include('statements.urls')),
    path('suppor/', include('support.urls')),
    path('userProfil/', include('userProfile.urls')),
    path('suppor/', include('support.urls')),
    path('nomine/', include('nomminee.urls')),
    path('api/', include('apii.urls')),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    



