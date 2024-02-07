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

        car1 = my_objects.car('green', 'honk honk')
        
        car2 = my_objects.car('blue', 'beep beep')


        the_context = {'hi':'hello universe!',
                       'name': new_name,
                       'orig_name' : my_name,
                       'names' : names,
                       'fixed_names' : fixed_names,
                       'car1' : car1,
                       'car2' : car2,
                       }

        return render(request, 'my_app/index.html',
                      the_context)