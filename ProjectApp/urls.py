from django.urls import path
from . import views

app_name = 'projectApp'
# urlpatterns = [
#     path('', views.Home, name='Home'), 
#     path('successfullREG/', views.SuccessfullREG, name='SuccessfullREG'),
#     path('profile/', views.profile, name='profile'),
#     path('editProfile/', views.editProfile, name='editProfile'), 
#     path('favorite/', views.favorite, name='favorite'), 
    
#     path('addMovie/', views.AddMovie, name='AddMovie'),
#     path('condributions/', views.Condributions, name='Condributions'),
#     path('chat/', views.Chat, name='Chat'),
#     path('viewMovie/<int:m_id>/', views.viewMovie, name='viewMovie'),

#     path('user_movies/', views.user_movies, name='user_movies'), 
#]

urlpatterns = [
    path('', views.Home, name='Home'), 
    path('successfullREG/', views.SuccessfullREG, name='SuccessfullREG'),
    path('profile/', views.profile, name='profile'),
    path('editProfile/', views.editProfile, name='editProfile'), 
    path('favorite/', views.favorite, name='favorite'), 
    path('addMovie/', views.AddMovie, name='AddMovie'),
    path('chat/', views.Chat, name='Chat'),
    path('edit_movie/<int:movie_id>/', views.edit_movie, name='edit_movie'), # Define URL pattern for edit_movie
    path('delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'), # Define URL pattern for delete_movie
    path('user_movies/', views.user_movies, name='user_movies'), 
    path('viewMovie/<int:m_id>/', views.viewMovie, name='viewMovie'),
    path('submit_review/', views.submit_review, name='submit_review'),

    path('showByCatogory/<str:m_catagory>/', views.showByCatogory, name='showByCatogory'),
    path('error/', views.error, name='error'),

]