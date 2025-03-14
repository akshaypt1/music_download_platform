from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('sign/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('upload/', views.upload_music, name='upload_music'),
    path('music/', views.music_list, name='music_list'),
    path('music/<int:music_id>/', views.music_detail, name='music_detail'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('logout/', views.logout_view, name='logout'),
      
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



