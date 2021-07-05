
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from . import views
from django.contrib import admin
 

app_name = 'uslugi'



urlpatterns = [
    path('', views.view_categoryes),
    path('created-regions/', views.create_regions, name='create_region'),
    path('leave_application/', views.application, name="application"), 
    path('<slug:slug>/', views.view_category, name='category'),
    path('<slug:slug_category>/<slug:slug_uslugi>/', views.view_children_category, name='children_category'),
    path('<slug:slug_category>/<slug:slug_children_category>/<slug_uslugi>/', views.view_uslugi, name='uslugi'),

    

    path('robots.txt', views.robots_txt, name = 'robots_txt'), 
]



if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
handler404 = 'uslugi.views.e_handler404'

