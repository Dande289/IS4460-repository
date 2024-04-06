from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from .models import Show, User, Actor, Award
from .forms import ShowForm, ActorForm, UserForm, AwardForm
from rest_framework import generics
from .serializers import ShowSerializer, UserSerializer, AwardSerializer

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
    def get(self, request, show_id=None):
        show = Show.objects.get(pk=show_id)
        return render(
            request=request,
            template_name='website/show_delete.html',
            context={'show': show}
        )

    def post(self, request, show_id):
        if 'confirm' in request.POST:
            show = Show.objects.get(pk=show_id)
            show.delete()
            return redirect("show-list")
        else:
            return redirect("show-detail", show_id=show_id)

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
        form = ActorForm(request.POST,)
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
    def get(self, request, actor_id=None):
        actor = Actor.objects.get(pk=actor_id)
        return render(
            request=request,
            template_name='website/actor_delete.html',
            context={'actor': actor}
        )

    def post(self, request, actor_id):
        if 'confirm' in request.POST:
            actor = Actor.objects.get(pk=actor_id)
            actor.delete()
            return redirect("actor-list")
        else:
            return redirect("actor-detail", actor_id=actor_id)

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
    
    
#AWARD VIEWS
class AwardAdd(View):
    def get(self, request):
        form = AwardForm()
        return render(request = request,
                      template_name='website/award_add.html',
                      context = {'form':form})
        
    def post(self, request):
        form = AwardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('award-list')  # Redirect to the award list page after adding
        return render(request=request,
                      template_name='website/award_add.html',
                      context={'form': form})

        
class AwardList(View):
    def get(self, request):
        awards = Award.objects.all()
        return render(request=request,
                      template_name='website/award_list.html',
                      context = {'awards':awards})

class AwardEdit(View):
    def get(self, request, award_id):
        award = Award.objects.get(pk=award_id)
        form = AwardForm(instance = award)
        
        return render(request=request,
                      template_name='website/award_edit.html',
                      context = {'award':award, 'form':form})
        
    def post(self,request,award_id):
       award=Award.objects.get(pk=award_id)
       form=AwardForm(request.POST,instance=award)
       
       if form.is_valid():
           award=form.save()
           return redirect('award-list')
       return render(request=request,
                     template_name='website/award_edit.html',
                     context={'award':award, 'form':form}) 

class AwardDetails(View):
    def get(self, request, award_id):
        award=Award.objects.get(pk=award_id)
        fields=award._meta.get_fields()
        return render(request=request,
                      template_name='website/award_details.html',
                      context={'award':award,'fields':fields})

class AwardDelete(View):
    def get(self, request, award_id=None):
        award=Award.objects.get(pk=award_id)
        return render(
            request=request,
            template_name='website/award_delete.html',
            context={'award':award}
        )
    def post(self,request,award_id):
        if 'confirm' in request.POST:
            award=Award.objects.get(pk=award_id)
            award.delete()
            return redirect('award-list')
        else:
            return redirect('award-detail',award_id=award_id)
            

class AwardListCreateView(generics.ListCreateAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    
