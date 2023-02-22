from django.urls import path, include

from .import views

from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




urlpatterns = [

       
    path('notes', views.notes_list, name='notes'),
    
    path('note/<int:pk>',views.note_detail, name='note'),
    
    path('register', views.register, name='register'),
    
    path('login', obtain_auth_token, name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)