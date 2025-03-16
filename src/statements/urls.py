from django.urls import path
from .views import *
urlpatterns = [

    
    #path('statement/',statement , name="statement"),
    path('statement/',StatementList.as_view() , name="statement"),
    # path('statement/download-pdf', pdf_generate , name="download_pdf"),

   
    
]
