from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .models import Show, User, Actor
from .forms import ShowForm, ActorForm, UserForm
from rest_framework import generics
from .serializers import ShowSerializer, UserSerializer

# Create your views here.
class Home(View):
    def get(self,request):

        return render(request=request,
                      template_name='website/home.html',
                      context={})
    

class ShowList(View):

    def get(self,request):

        shows = Show.objects.all()

        return render(request = request,
                      template_name = 'website/show_list.html',
                      context = {'shows':shows})
    
class ShowEdit(View):

    def get(self,request,show_id):

        show = Show.objects.get(pk=show_id)
        form = ShowForm(instance=show)

        return render(request = request,
                      template_name = 'website/show_edit.html',
                      context = {'show':show,'form':form})
    
    def post(self,request,show_id):

        show = Show.objects.get(pk=show_id)
        form = ShowForm(request.POST,instance=show)

        if form.is_valid():
            show = form.save()
            return redirect('show-list')

        return render(request = request,
                      template_name = 'website/show_edit.html',
                      context = {'show':show,'form':form})
    
class ShowAdd(View):
    def get(self, request):
        form = ShowForm()
        return render(request = request, 
                      template_name = 'website/show_add.html',
                      context = {'form':form})
    
    def post(self, request):
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-list')
        return render(request = request,
                      template_name = 'website/show_add.html', 
                      context={'form': form})
    

class ShowDetails(View):
    def get(self, request, show_id):
        show = Show.objects.get(pk=show_id)
        fields = show._meta.get_fields()
        return render(request=request, 
                      template_name='website/show_detail.html', 
                      context={'show': show, 'fields':fields})

    

class ShowDelete(View):
    def get(self,request,show_id=None):

         show = Show.objects.get(pk=show_id)
         form = ShowForm(instance=show)

         return render(request = request,
                       template_name = 'website/show_delete.html',
                       context = {'show':show,'form':form})

    def post(self,request,show_id):
        show = Show.objects.get(pk=show_id)
        show.delete()
        return redirect("show-list")
    

class ActorList(View):

    def get(self,request):

        actors = Actor.objects.all()

        return render(request = request,
                      template_name = 'website/actor_list.html',
                      context = {'actors':actors})
    
class ActorEdit(View):

    def get(self,request,actor_id):

        actor = Actor.objects.get(pk=actor_id)
        form = ActorForm(instance=actor)

        return render(request = request,
                      template_name = 'website/actor_edit.html',
                      context = {'actor':actor, 'form':form})

    def post(self,request,actor_id):

        actor = Actor.objects.get(pk=actor_id)
        form = ActorForm(request.POST,instance=actor)

        if form.is_valid():
            actor = form.save()
            return redirect('actor-list')
        
        return render(request = request,
                      template_name = 'website/actor_edit.html',
                      context = {'actor':actor, 'form':form})
    
class ActorAdd(View):
    def get(self, request):
        form = ActorForm()
        return render(request = request,
                      template_name = 'website/actor_add.html',
                      context = {'form':form})
    
    def post(self, request):
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actor-list')
        return render(request = request,
                      template_name = 'website/actor_add.html',
                      context={'form': form})
    
class ActorDetails(View):
    def get(self, request, actor_id):
        actor = Actor.objects.get(pk=actor_id)
        fields = actor._meta.get_fields()
        return render(request=request, 
                      template_name='website/actor_detail.html', 
                      context={'actor': actor, 'fields':fields})

    

class ActorDelete(View):
    def get(self,request,actor_id=None):

         actor = Actor.objects.get(pk=actor_id)
         form = ActorForm(instance=actor)

         return render(request = request,
                       template_name = 'website/actor_delete.html',
                       context = {'actor':actor,'form':form})

    def post(self,request,actor_id):
        actor = Show.objects.get(pk=actor_id)
        actor.delete()
        return redirect("actor-list")


class ShowListCreateView(generics.ListCreateAPIView):

    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class ShowDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class UserListCreateView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    