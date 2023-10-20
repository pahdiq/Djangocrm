
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('viewer/', views.viewer, name='viewer'),
    path('aboutUs/' , views.aboutUs, name='aboutUs'),
    path('contactUs/' , views.contactUs, name='contactUs'),
    path('adder/', views.adder, name='adder'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
