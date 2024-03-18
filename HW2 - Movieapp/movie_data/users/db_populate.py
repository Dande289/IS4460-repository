import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','movie_data.settings')
django.setup()

from users.models import Movie

#Delete Movies --> Use for loop
models_to_clear = [Movie]
for model_class in models_to_clear:
    for instance in model_class.objects.all():
        instance.delete()

movie_list = ['Avatar','Toy Story','The Matrix','Good Will Hunting','Forgetting Sarah Marshall','Step Brothers','Shrek','Waynes World','Austin Powers','A Bugs Life']
for movie in movie_list:
    my_new_movie = Movie()
    my_new_movie.title = movie
    my_new_movie.save()

#Django QuerySet statements for Movie
all_movies = Movie.objects.all()

movies_filter = Movie.objects.filter(title__startswith='Toy')

#get_movie = Movie.objects.get(id=1)

#update_movie = Movie.objects.get(id=4)
#update_movie.title = "New Movie Title"
#update_movie.save()

#delete_movie = Movie.objects.get(id=3)
#delete_movie.delete()

from users.models import User

models_to_clear = [User]
for model_class in models_to_clear:
    for instance in model_class.objects.all():
        instance.delete()

my_new_user = User()
my_new_user.username = "username1"
my_new_user.password = "password1"
my_new_user.first_name = "Dillon"
my_new_user.last_name = "Anderson"
my_new_user.email = "test@test.com"
my_new_user.save()
my_new_user_2 = User()
my_new_user_2.username = "username2"
my_new_user_2.password = "password2"
my_new_user_2.first_name = "Robert"
my_new_user_2.last_name = "Anderson"
my_new_user_2.email = "test2@test.com"
my_new_user_2.save()
my_new_user_3 = User()
my_new_user_3.username = "username3"
my_new_user_3.password = "password3"
my_new_user_3.first_name = "Collin"
my_new_user_3.last_name = "Anderson"
my_new_user_3.email = "test3@test.com"
my_new_user_3.save()

from users.models import Role

models_to_clear = [Role]
for model_class in models_to_clear:
    for instance in model_class.objects.all():
        instance.delete()

my_new_role = Role()
my_new_role.username = "userrole1"
my_new_role.role = "Admin"
my_new_role.save()
