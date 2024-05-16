from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from . models import Movie
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

def Home(request):
    allMovie = Movie.objects.all()
    return render(request,'user/Home.html',{'allMovie':allMovie})

def SuccessfullREG(request):
    return render(request,'user/SuccessfullREG.html')

@login_required
def AddMovie(request):
    if request.method == 'POST':
        name = request.POST.get('title',)
        decription = request.POST.get('description',)
        year = request.POST.get('release',)
        actors1 = request.POST.get('actors1',)
        actors2 = request.POST.get('actors2',)
        actors3 = request.POST.get('actors3',)
        category = request.POST.get('category',)
        link = request.POST.get('trailer',)

        if 'youtu.be' in link:
            video_id = link.split('/')[-1].split('?')[0]
        elif 'watch?v=' in link:
            video_id = link.split('=')[-1].split('&')[0]
        else:
            video_id = link

        # Save movie with extracted video ID
        image = request.FILES['poster']
        movie = Movie(user=request.user,name=name, category=category, link=video_id, description=decription,actors_1=actors1, actors_2=actors2,actors_3=actors3, date=year, image_1=image)
        movie.save()
        return redirect('/')
    return render(request,'user/addMovie.html')

# @login_required
def user_movies(request):
    usr = request.user
    user_movies = []
    if usr.is_authenticated:
        user_movies = Movie.objects.filter(user=request.user)
    return render(request, 'user/user_movies.html', {'user_movies': user_movies})

from django.shortcuts import get_object_or_404

@login_required
def edit_movie(request, movie_id):
    # Retrieve the movie object to edit
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'POST':
        # Update movie details based on form data
        movie.name = request.POST.get('title')
        movie.description = request.POST.get('description')
        movie.year = request.POST.get('release')
        movie.actors1 = request.POST.get('actors1')
        movie.actors2 = request.POST.get('actors2')
        movie.actors3 = request.POST.get('actors3')
        movie.category = request.POST.get('category')
        movie.link = extract_video_id(request.POST.get('trailer'))

        # Check if a new poster image is uploaded
        if 'poster' in request.FILES:
            movie.image_1 = request.FILES['poster']

        # Save the updated movie object
        movie.save()

        # Redirect to the user's movie list or any other appropriate page
        user_movies_url = reverse('projectApp:user_movies')  # Replace 'auth_app' with your app's name (make redirec dynamic)
        return redirect(user_movies_url)


    # Render the edit movie form with the existing movie details
    return render(request, 'user/edit_movie.html', {'movie': movie})

def extract_video_id(link):
    if 'youtu.be' in link:
        return link.split('/')[-1].split('?')[0]
    elif 'watch?v=' in link:
        return link.split('=')[-1].split('&')[0]
    else:
        return link


from django.shortcuts import get_object_or_404

@login_required
def delete_movie(request, movie_id):
    # Retrieve the movie object or return 404 if not found
    movie = get_object_or_404(Movie, pk=movie_id)

    # Check if the logged-in user is the owner of the movie
    if request.user == movie.user:
        # Delete the movie
        movie.delete()
        # Redirect to user_movies page or any other appropriate page after deletion
        return redirect('projectApp:user_movies')
    else:
        # If the logged-in user is not the owner of the movie, return 403 Forbidden
        return HttpResponseForbidden("You don't have permission to delete this movie.")


def profile(request):
    return render(request,'user/profile.html')

def editProfile(request):
    return render(request,'user/editProfile.html')

def favorite(request):
    return render(request,'user/Home.html')

def Chat(request):
    return render(request,'user/chat.html')

from .models import MovieReview

def viewMovie(request, m_id):
    id_obj = Movie.objects.get(id=m_id)
    reviews = MovieReview.objects.filter(movie_name=id_obj).order_by('-created')
    return render(request, 'user/viewMovie.html', {'movie': id_obj, 'reviews': reviews})

from .models import MovieReview

def submit_review(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        movie_name = request.POST.get('movie_name')
        review_text = request.POST.get('review_text')
        rating = request.POST.get('rating')

        # Create and save the review object
        review = MovieReview(movie_name=movie_name, review_text=review_text, rating=rating, user_name=user_name)
        review.save()
        return redirect('projectApp:viewMovie')
    else:
        return redirect('user/error.html')  # Redirect to an error page if not a POST request

#//------------------------------------------------

def showByCatogory(request, m_catagory):
    catogory_movies = Movie.objects.filter(category=m_catagory)
    print(catogory_movies)
    return render(request,'user/category.html',{'movies': catogory_movies})

def error(request):
    return render(request,'user/error.html')