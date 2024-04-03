from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .models import Movie, User
from .forms import MovieForm, UserForm
from rest_framework import generics
from .serializers import MovieSerializer, UserSerializer

# Create your views here.
class MovieList(View):

    def get(self,request):

        movies = Movie.objects.all()

        return render(request = request,
                      template_name = 'movie/movie_list.html',
                      context = {'movies':movies})
    
class MovieEdit(View):

    def get(self,request,movie_id):

        movie = Movie.objects.get(pk=movie_id)
        form = MovieForm(instance=movie)

        return render(request = request,
                      template_name = 'movie/movie_edit.html',
                      context = {'movie':movie,'form':form})
    
    def post(self,request,movie_id):

        movie = Movie.objects.get(pk=movie_id)
        form = MovieForm(request.POST,instance=movie)

        if form.is_valid():
            movie = form.save()
            return redirect('movie-list')

        return render(request = request,
                      template_name = 'movie/movie_edit.html',
                      context = {'movie':movie,'form':form})
    
class MovieAdd(View):
    def get(self, request):
        form = MovieForm()
        return render(request = request, 
                      template_name = 'movie/movie_add.html',
                      context = {'form':form})
    
    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
        return render(request = request,
                      template_name = 'movie/movie_add.html', 
                      context={'form': form})
    

class MovieDetails(View):
    def get(self, request, movie_id):
        movie = Movie.objects.get(pk=movie_id)
        fields = movie._meta.get_fields()
        return render(request=request, 
                      template_name='movie/movie_details.html', 
                      context={'movie': movie, 'fields':fields})

    

class MovieDelete(View):
    def get(self,request,movie_id=None):

         movie = Movie.objects.get(pk=movie_id)
         form = MovieForm(instance=movie)

         return render(request = request,
                       template_name = 'movie/movie_delete.html',
                       context = {'movie':movie,'form':form})

    def post(self,request,movie_id):
        movie = Movie.objects.get(pk=movie_id)
        movie.delete()
        return redirect("movie-list")

class MovieListCreateView(generics.ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class UserListCreateView(generics.ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    