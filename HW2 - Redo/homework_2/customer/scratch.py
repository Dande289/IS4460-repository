from customer.models import Movie


#4. Write Django QuerySet statements for Movie:


#Retrieve all movies
all_movies = Movie.objects.all()
print(all_movies)


#Filter for movies starting with some text
movie_filter = Movie.objects.filter(title="Toy Story")
print(movie_filter)


#Get one movie
get_movie = Movie.objects.get(title="Austin Powers")
print(get_movie)


#Update one movie
update_movie = Movie.objects.get(title="Austin Powers")
update_movie.director = "Jay Roach"
update_movie.save()


#Delete one movie
delete_movie = Movie.objects.get(title="Austin Powers")
delete_movie.delete()


from customer.models import User

#5. Write Django model statements for User model:

 
user_model = User.objects.get(username = "username2")
print(f"Username:{user_model.username}")
print(f"First name: {user_model.first_name}")
print(f"Last name: {user_model.last_name}")
print(f"Email: {user_model.email}")
