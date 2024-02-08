from django.views import View
from django.shortcuts import render, redirect
from . import my_functions, my_objects

def title_name(the_name: str):
    return the_name.title()

class HomePageView(View):
    def get(self, request):

        my_name = "dILLON"

        new_name = title_name(my_name)

        names = ['Dillon', 'Robert','Brayden']

        fixed_names = my_functions.fix_names_list(names)

        car1 = my_objects.car(color = 'green', sound = 'honk honk')
        
        car2 = my_objects.car(color = 'blue', sound = 'beep beep')

        motorcycle1 = my_objects.motorcycle(color = '', sound = '', make = 'Husqvarna', year = '2018')

        the_context = {'hi':'hello universe!',
                       'name': new_name,
                       'orig_name' : my_name,
                       'names' : names,
                       'fixed_names' : fixed_names,
                       'car1' : car1,
                       'car2' : car2,
                       'motorcycle1' : motorcycle1,
                       }

        return render(request, 'my_app/index.html',
                      the_context)