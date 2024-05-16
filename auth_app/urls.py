from . import views
from django.urls import path

app_name = 'auth_app'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]