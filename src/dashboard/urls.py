from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static


urlpatterns = [
    
    
    path('dj-admin/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
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
    path('loan/', include('loan.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


