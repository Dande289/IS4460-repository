from django.views import View
from django.shortcuts import render, redirect


def title_name(the_name: str):
    return the_name.title()

class HomePageView(View):
    def get(self, request):

        my_name = "dILLON"

        new_name = title_name(my_name)

        names = ['Dillon', 'Robert','Brayden']

        the_context = {'hi':'hello universe!',
                       'name': new_name,
                       'orig_name' : my_name,
                       'names' : names
                       }

        return render(request, 'my_app/index.html',
                      the_context)